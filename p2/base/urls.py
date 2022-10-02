from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.bienvenida, name="bienvenida"),
    path('listacursos/', views.listacursos, name="listacursos"),
    path('actualizar-curso/<str:pk>/', views.actualizarCurso, name="actualizar-curso"),
    path('eliminar-curso/<str:pk>/', views.eliminarCurso, name="eliminar-curso"),
    path('curso/<str:pk>/', views.curso, name="curso"),
    path('crear-estudiante/<str:pk>/', views.crearEstudiante, name="crear-estudiante"),
    path('actualizar-estudiante/<str:pk>/', views.actualizarEstudiante, name="actualizar-estudiante"),
    path('eliminar-estudiante/<str:pk>/', views.eliminarEstudiante, name="eliminar-estudiante"),
    path('listapruebas/', views.listapruebas, name="listapruebas"),
    path('actualizar-prueba/<str:pk>/', views.actualizarPrueba, name="actualizar-prueba"),
    path('eliminar-prueba/<str:pk>/', views.eliminarPrueba, name="eliminar-prueba"),
    path('prueba/<str:pk>/', views.prueba, name="prueba"),
    path('crear-preguntas/<str:pk>/', views.crearPreguntas, name="crear-preguntas"),
    path('actualizar-preguntas/<str:pk>/', views.actualizarPreguntas, name="actualizar-preguntas"),
    path('eliminar-preguntas/<str:pk>/', views.eliminarPreguntas, name="eliminar-preguntas"),
    path('pregunta/<str:pk>/', views.pregunta, name="pregunta"),
    path('relacionar-preguntas/<str:pk>/', views.relacionarPreguntas, name="relacionar-preguntas"),
    path('eliminar-relacion-preguntas/<str:pk>/', views.eliminarRelacionPreguntas, name="eliminar-relacion-preguntas"),
    path('listatemas/', views.listatemas, name="listatemas"),
    path('actualizar-tema/<str:pk>/', views.actualizarTema, name="actualizar-tema"),
    path('eliminar-tema/<str:pk>/', views.eliminarTema, name="eliminar-tema"),
]