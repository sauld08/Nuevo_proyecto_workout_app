from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('signup/', views.signup, name='signup'),
=======
>>>>>>> 483c967e976a71a3af2c5b67effc6fd16594fb9a
    path('', views.HomeView.as_view(), name='home'),
    path('grupo/<int:pk>/', views.GrupoMuscularDetailView.as_view(), name='grupo_muscular_detalle'),
    path('ejercicio/nuevo/', views.EjercicioCreateView.as_view(), name='ejercicio_nuevo'),
    path('ejercicio/<int:pk>/editar/', views.EjercicioUpdateView.as_view(), name='ejercicio_editar'),
    path('ejercicio/<int:pk>/eliminar/', views.EjercicioDeleteView.as_view(), name='ejercicio_eliminar'),
]