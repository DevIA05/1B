"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from quiz.views import index

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Custom Decoration: Prevent access to the page
def notAccessForCollaborateur(function):
    def wrapper(request, *args, **kw):
        user=request.user 
        if(not user.isSuperUser()):
            return HttpResponseRedirect('/unauthorized/')
        else:
            return function(request, *args, **kw)
    return wrapper


# Customizing error views
# https://docs.djangoproject.com/en/dev/topics/http/views/#customizing-error-views
handler404 = 'quiz.views.redirectPNF'

urlpatterns = [
    path('',index, name="index"),
    path('admin/', admin.site.urls),
    path('quiz/home', views.home, name="home"),
    path('quiz', include('django.contrib.auth.urls')),
    path('quiz/', include('identification.urls')),
    path('p1', login_required()(views.page1), name="p1"),
    path('p2', login_required()(notAccessForCollaborateur(views.page2)), name="p2"),
    path('p3', views.page3, name="p3"),
    path('quiz/q', views.quiz, name="quiz"),
    path('appSuperUser/', include("appSuperUser.urls")),
    path('quizz/', include('appCollab.urls')),
]

