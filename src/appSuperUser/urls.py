from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('gestion-session', views.tbd, name='tbd'),
    path('uploadQuizz/', views.uploadQuizz, name='uploadQuizz'),
    path('ajout-personnel/', views.addDataInDB, name='ajoutEmp'),
    re_path(r'^addDataInDB$', views.addDataInDB, name='addDataInDB'),
    path('accueil', views.pa, name='pa'),    
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)