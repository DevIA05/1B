from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from quiz.models import Collaborateur, Superuser

typeUser = -1; # 0  collaborateur
               # 1  chef de secteur ou super user
               # -1 anonyme 

# Create your views here.
def login_user(request):
    if request.method == "POST":
        matricule = request.POST['matricule']
        password = request.POST['password']
        if(checkEmployee(matricule)): user = authenticate(request, matricule=matricule, password=password)
        print(user)
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

def checkEmployee(matricule, typeUser):
    isVerified = False
    if(typeUser == 1):
        if(len(Collaborateur.objects.filter(matricule=matricule))==1): 
            isVerified = True
    if(typeUser == 2):
        if(len(Superuser.objects.filter(matricule=matricule))==1):
            isVerified = True
    return isVerified


