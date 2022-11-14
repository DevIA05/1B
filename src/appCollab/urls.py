from django.urls import path
from . import views

urlpatterns = [
    path('collab/accueil', views.pa1, name='pa1'),
    path('collab/session', views.ce, name="ce"),
    path('collab/quiz', views.doTheQuiz),
]