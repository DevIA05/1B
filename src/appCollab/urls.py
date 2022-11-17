from django.urls import path, re_path
from . import views

urlpatterns = [
    path('accueil', views.pa1, name='pa1'),
    path('session', views.ce, name="ce"),
    path('quizz', views.initQuiz, name="quiz"),
    re_path(r'^nextQuestion$', views.nextQuestion)
]