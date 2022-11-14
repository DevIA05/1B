from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import xmltodict, json, os, glob, shutil
from os import walk,listdir
from os.path import isfile, join
from pathlib import Path
from quiz.models import Quizz
from django.contrib.auth.decorators import login_required
from quiz.models import Personnel, Collaborateur, Superuser, Secteur


def tbd(request):
    template = loader.get_template ('tbd_sc.html')
    return HttpResponse(template.render())

def pa(request):
    template = loader.get_template ('page_aut.html')
    return HttpResponse(template.render())

@login_required
def uploadQuizz(request):
    monRepertoireQ = 'questionnaires/'
    monRepertoireTemp = 'qjsonTemp/'
    monRepertoire='qjson/'
    context ={}
    delete(monRepertoireTemp),
    delete(monRepertoireQ),
    if request.method =='POST':
        for f in request.FILES.getlist('document'):
            quizz=f
            # print(str(f))
            fs=FileSystemStorage()
            fs.save(quizz.name,quizz)           
        exec(open("script/xmljson.py").read())
        listeFichiers=[f for f in listdir(monRepertoireTemp) if isfile(join(monRepertoireTemp,f))]
        urlFichiers=[monRepertoire + f for f in listeFichiers]
        context['noms']=listeFichiers    
        for i in range(len(listeFichiers)):
            nQ= Quizz(nomfichier=listeFichiers[i], urlfichier = urlFichiers[i])
            nQ.save()           
    #     return redirect('uploadQuizz')
    # else:
    return render(request,'uploadQuizz.html', context=context)


def delete(dossier):
    for root, dirs, files in os.walk(dossier):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))


# def addEmp(request):
#     return render(request, 'addEmployee.html', {})

def addEmp(request):
    return render(request, 'addEmployee.html', {})

def addDataInDB(request):
    if request.method == "POST": 
        #import pdb; pdb.set_trace()
        # print(request.POST)
        for i in range(1, ((len(request.POST)-1)//4)+1): # on ne prend pas la valeur csrfmiddlewaretoken. 
                                                    # Il y a pour l'instant quatres colonnes.
            matricule = request.POST['result['+str(i)+'][matricule]']
            prenom    = request.POST['result['+str(i)+'][prenom]'] 
            nom       = request.POST['result['+str(i)+'][nom]'] 
            password  = request.POST['result['+str(i)+'][password]'] 
            p = Personnel.objects.create_user(prenom=prenom, nom=nom, matricule=matricule, codesecteur="MKT", password=password); p.save()
            c = Collaborateur.objects.create(matricule=Personnel.objects.get(pk=matricule)); c.save()
        #import pdb; pdb.set_trace()
    return render(request, 'addEmployee.html')
