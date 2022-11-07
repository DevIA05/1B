from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name="login"),
    path('', views.logout_user, name="logout"),
    path('pa', views.page_aut, name="page_aut")
]
