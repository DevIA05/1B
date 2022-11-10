from django.urls import path, re_path
from . import views

urlpatterns =[
    path('', views.tbd, name='tbd'),
    path('ae', views.addEmp, name='ajoutEmp'),
    re_path(r'^addDataInDB$', views.addDataInDB, name='addDataInDB')
]

