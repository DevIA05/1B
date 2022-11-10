from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def tbd(request):
    template = loader.get_template ('tbd_sc.html')
    return HttpResponse(template.render())


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