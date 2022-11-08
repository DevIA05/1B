from django.http import HttpResponse
from django.template import loader

def pa1(request):
    template = loader.get_template ('page_accueil.html')
    return HttpResponse(template.render())

def ce(request):
    template = loader.get_template ('condi_exam.html')
    return HttpResponse(template.render())