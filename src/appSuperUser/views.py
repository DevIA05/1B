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

# def addDataInDB(request):
#     if request.method == "POST":
#         print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
    #     matricule = request.POST['matricule']
    #     result = request.GET.get('result', None)
    #     print(result)
    # # Any process that you want
    #     data = {
    #         # Data that you want to send to javascript function
    # }
    # return JsonResponse(data)

