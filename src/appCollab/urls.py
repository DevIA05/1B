from django.urls import path
from . import views

urlpatterns = [
    path('', views.pa1, name='pa1'),
    path('ce', views.ce, name="ce"),
]