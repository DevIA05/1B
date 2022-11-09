from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def tbd(request):
    template = loader.get_template ('tbd_sc.html')
    return HttpResponse(template.render())


def addEmp(request):
    return render(request, 'addEmployee.html', {})