from django.http import HttpResponse
from django.template import loader

def tbd(request):
    template = loader.get_template ('tbd_sc.html')
    return HttpResponse(template.render())

def pa(request):
    template = loader.get_template ('page_aut.html')
    return HttpResponse(template.render())