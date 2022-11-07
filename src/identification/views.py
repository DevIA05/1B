from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from quiz.models import Collaborateur, Superuser
from django.template import loader

# Create your views here.
def login_user(request):
    if request.method == "POST":
        matricule = request.POST['matricule']
        password = request.POST['password']
        user = authenticate(request, matricule=matricule, password=password)
        if user is not None:
            login(request, user)
            return redirect('p1')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('login')
    else:
        return render(request, 'identification/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('login')

def page_aut(request):
    template = loader.get_template ('page_aut.html')
    return HttpResponse(template.render())
