from django.urls import path
from . import views

urlpatterns =[
    path('', views.tbd, name='tbd'),
    path('ae', views.addEmp, name='ajoutEmp'),
]

