from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from quiz.models import Quizz, Personnel, Collaborateur, Superuser
import json, os

def pa1(request):
    return render(request, 'page_accueil.html')

def ce(request):
    return render(request, 'condi_exam.html')


# def loadQuiz(request):
    # data = {'@goodResp': '3', '@time': '00:00:30.00', '@coeff': '1', 
    #         'title': "title", 
    #         'question': 'q1 :', 
    #         'listeResp': {'response': ['resp1', 'resp2', 'resp3']}}
    # with open("qjson/31.quv.json") as f: data = json.load(f)
    # request.session['task_created'] = "ok"
    # quizHTML(data, 0)

def quizHTML(request):
    with open("qjson/31.quv.json") as f: data = json.load(f)
    request.session['pointsDuCandidat'] = 0
    request.session['quiz'] = data
    numQuestion = 0
    duree       = convertTimeToMin(data["questionnaire"]["question"][numQuestion]["@duree"])
    titre       = data["questionnaire"]["question"][numQuestion]["titre"]
    intitule    = data["questionnaire"]["question"][numQuestion]["intitule"]
    reponses    = data["questionnaire"]["question"][numQuestion]['listerep']["reponse"]
    nbReponses  = list(range(1, len(reponses)+1))
    # coeff       = data["questionnaire"]["question"][numQuestion]["@coeff"]
    # bonneRep    = data["questionnaire"]["question"][numQuestion]["@bonne"]

    return render(request, 'doTheQuiz.html', context={"duree"       : duree,
                                                      "titre"       : titre,
                                                      "intitule"    : intitule,
                                                      "reponses"    : zip(reponses, nbReponses),
                                                      "numQuestion" : numQuestion})

def nextQuestion(request):
    if request.method == "POST":
        checkedBox = request.POST.getlist('result[]')
        print(checkedBox)
        numQuestion += 1
        #getQuiz = Quizz.objects.get(idquizz=2)  
        q = loadQuiz()
        return quizHTML()

def convertTimeToMin(t): 
    s = t.split(':'); 
    min = float(s[0])*60+float(s[1])+float(s[2])/60; 
    return min