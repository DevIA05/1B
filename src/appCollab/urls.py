from django.urls import path, re_path
from . import views

urlpatterns = [
    path('accueil', views.pa1, name='accueilCollab'),
    path('session/<int:idsession>', views.ce, name="conditionExamen"),
    path('quizz', views.initQuiz, name="quizReal"),
    re_path(r'^nextQuestion$', views.nextQuestion),
    path('score',views.score,name='score'),
]