from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from quiz.models import Quizz, Personnel, Collaborateur, Superuser, Sessionquizz
import json, os
from django.http import JsonResponse
import pdb
from django.urls import reverse

def pa1(request):
    session=Sessionquizz.objects.all().values()
    context={'session':session}
    return render(request, 'page_accueil.html',context)
    

def ce(request, idsession):
    session= Sessionquizz.objects.get(idsession=idsession)
    context={'session':session}
    print(idsession)
    return render(request, 'condi_exam.html',context)


def initQuiz(request):
    with open("qjson/31.quv.json") as f: data = json.load(f)
    request.session['pointsDuCandidat'] = 0
    request.session['quiz'] = data
    request.session['numQuestion'] = 0
    context = dataToDict(request.session.get('quiz'), request.session.get('numQuestion'))

    return render(request, 'doTheQuiz.html', context=context)
    # coeff       = data["questionnaire"]["question"][numQuestion]["@coeff"]
    # bonneRep    = data["questionnaire"]["question"][numQuestion]["@bonne"]

def nextQuestion(request):
    if request.method == "POST":
        data = request.session.get("quiz")
        request.session["numQuestion"] = request.session.get('numQuestion') + 1
        context = dataToDict(data, request.session.get('numQuestion'))
        return JsonResponse({"data":context})


def dataToDict(data, numQuestion):
    duree       = convertTimeToMin(data["questionnaire"]["question"][numQuestion]["@duree"])
    titre       = data["questionnaire"]["question"][numQuestion]["titre"]
    intitule    = data["questionnaire"]["question"][numQuestion]["intitule"]
    reponses    = data["questionnaire"]["question"][numQuestion]['listerep']["reponse"]
    context={"duree"       : duree,
             "titre"       : titre,
             "intitule"    : intitule,
             "reponses"    : reponses}
    return context

def convertTimeToMin(t): 
    s = t.split(':'); 
    min = float(s[0])*3600+float(s[1])*60+float(s[2]);  
    return min