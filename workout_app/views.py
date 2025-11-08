from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .forms import SignUpForm
from .models import GrupoMuscular, Ejercicio, Comment
from .forms import CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

class HomeView(ListView):
    model = GrupoMuscular
    template_name = 'home.html'
    context_object_name = 'grupos_musculares'

class GrupoMuscularDetailView(DetailView):
    model = GrupoMuscular
    template_name = 'grupo_muscular_detalle.html'
    context_object_name = 'grupo_muscular'

class EjercicioCreateView(LoginRequiredMixin, CreateView):
    model = Ejercicio
    template_name = 'ejercicio_form.html'
    # Remove 'imagen_url', 'orden' and 'musculos_trabajados' from the creation form per UX requirement
    fields = ['nombre', 'descripcion', 'grupo_muscular', 'imagen']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # assign the author to the logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)

class EjercicioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ejercicio
    template_name = 'ejercicio_form.html'
    # Keep edit form consistent with create: remove 'imagen_url', 'orden' and 'musculos_trabajados'
    fields = ['nombre', 'descripcion', 'grupo_muscular', 'imagen']
    success_url = reverse_lazy('home')

    def test_func(self):
        ejercicio = self.get_object()
        return ejercicio.author == self.request.user

class EjercicioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ejercicio
    template_name = 'ejercicio_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        ejercicio = self.get_object()
        return ejercicio.author == self.request.user

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):
    """Show a confirmation page on GET and log the user out on POST."""
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'registration/logged_out.html')


class EjercicioDetailView(DetailView):
    model = Ejercicio
    template_name = 'ejercicio_detail.html'
    context_object_name = 'ejercicio'


@login_required
def comentario_nuevo(request, ejercicio_pk):
    ejercicio = get_object_or_404(Ejercicio, pk=ejercicio_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.ejercicio = ejercicio
            comment.save()
    return redirect(ejercicio.get_absolute_url())


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comentario_form.html'

    def get_success_url(self):
        return self.object.ejercicio.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comentario_confirm_delete.html'

    def get_success_url(self):
        return self.object.ejercicio.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
