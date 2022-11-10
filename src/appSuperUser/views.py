from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import xmltodict, json, os, glob
from os import walk
from pathlib import Path
from quiz.models import Quizz


def tbd(request):
    template = loader.get_template ('tbd_sc.html')
    return HttpResponse(template.render())

def uploadQuizz(request):
    context ={}
    if request.method =='POST':
        for f in request.FILES.getlist('document'):
            quizz=f
            # print(str(f))
            fs=FileSystemStorage()
            fs.save(quizz.name,quizz)
            context['nom']= quizz.name
            # print(url)       
        exec(open("script/xmljson.py").read())
        add()
        # uploadedFile = request.FILES['document']
        # print(type(uploadedFile))
        # print(uploadedFile.name)
        # print(uploadedFile.size)
        # fs = FileSystemStorage()
        # fs.save(uploadedFile.name, uploadedFile)
        # context['nom']= uploadedFile.name
        # context['url']=fs.url(name)
    return render(request,'uploadQuizz.html', context)

def  getListeFichiers(dossier) :
    listeFichiers = []
    for (repertoire, sousRepertoires, fichiers) in walk(dossier):
        listeFichiers.extend(fichiers)
        break                            
    # print(listeFichiers)
    return listeFichiers

monRepertoire = 'qjson/'
listeFichiers = getListeFichiers(monRepertoire)
# print(listeFichiers)

urlFichiers=[monRepertoire + f for f in listeFichiers]
# print(urlFichiers)



def add():
    for i in range(len(listeFichiers)):
        nQ= Quizz(nomfichier=listeFichiers[i], urlfichier = urlFichiers[i])
        nQ.save()

      
# def delete():
#     files=glob.glob('/questionnaires')
#     for f in files:
#         os.remove(f)     

def addEmp(request):
    return render(request, 'addEmployee.html', {})

def addDataInDB(request):
    if request.method == "POST":
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
    #     matricule = request.POST['matricule']
    #     result = request.GET.get('result', None)
    #     print(result)
    # # Any process that you want
    #     data = {
    #         # Data that you want to send to javascript function
    # }
    # return JsonResponse(data)
