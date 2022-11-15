from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from quiz.models import Quizz, Personnel, Collaborateur, Superuser
import json

def pa1(request):
    return render(request, 'page_accueil.html')

def ce(request):
    return render(request, 'condi_exam.html')



def doTheQuiz(request):
    getQuiz = Quizz.objects.get(idquizz=2)    
    with open(getQuiz.urlfichier) as f: data = json.load(f)
    
    duree      = convertTimeToMin(data["questionnaire"]["question"][0]["@duree"])
    titre      = data["questionnaire"]["question"][0]["titre"]
    intitule   = data["questionnaire"]["question"][0]["intitule"]
    reponses   = data["questionnaire"]["question"][0]['listerep']["reponse"]
    nbReponses = list(range(1, len(reponses)+1))
    
    return render(request, 'doTheQuiz.html', context={"duree"    : duree,
                                                      "titre"    : titre,
                                                      "intitule" : intitule,
                                                      "reponses" : zip(reponses, nbReponses)})


def convertTimeToMin(t): 
    s = t.split(':'); 
    min = float(s[0])*60+float(s[1])+float(s[2])/60; 
    return min