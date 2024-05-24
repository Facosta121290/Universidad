from django.urls import path
from . import views

app_name = "Academico"


urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path("", views.home, name="home"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
]