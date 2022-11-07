from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template ('intranet/test.html')
    return HttpResponse(template.render())

def quiz(request):
    template = loader.get_template ('quiz/p1.html')
    return HttpResponse(template.render())
# Create your views here.
