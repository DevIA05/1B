from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', views.tbd, name='tbd'),
    path('uploadQuizz/', views.uploadQuizz, name='uploadQuizz'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)