from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', views.tbd, name='tbd'),
    path('uploadQuizz/', views.uploadQuizz, name='uploadQuizz'),
    path('ae', views.addEmp, name='ajoutEmp'),
    re_path(r'^addDataInDB$', views.addDataInDB, name='addDataInDB'),
    path('pa', views.pa, name='pa'),
    path('upload', views.upload, name="upload"),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)