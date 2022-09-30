from django.urls import path
from . import views

urlpatterns = [
path('', views.login, name='core'),
path('principal', views.principal, name='principal'),
path('registro', views.registro, name='registro'),
path('doctor',views.doctor, name='doctor')
]
