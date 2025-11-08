from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .forms import SignUpForm
from .models import GrupoMuscular, Ejercicio

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
    fields = ['nombre', 'descripcion', 'grupo_muscular', 'musculos_trabajados', 'imagen', 'imagen_url', 'orden']
    success_url = reverse_lazy('home')

class EjercicioUpdateView(LoginRequiredMixin, UpdateView):
    model = Ejercicio
    template_name = 'ejercicio_form.html'
    fields = ['nombre', 'descripcion', 'grupo_muscular', 'musculos_trabajados', 'imagen', 'imagen_url', 'orden']
    success_url = reverse_lazy('home')

class EjercicioDeleteView(LoginRequiredMixin, DeleteView):
    model = Ejercicio
    template_name = 'ejercicio_confirm_delete.html'
    success_url = reverse_lazy('home')

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
