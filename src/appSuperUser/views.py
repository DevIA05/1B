from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

def tbd(request):
    template = loader.get_template ('tbd_sc.html')
    return HttpResponse(template.render())

def uploadQuizz(request):
    context ={}
    if request.method =='POST':
        # for f in request.FILES.getlist('document'):
        #     print(str(f))
        # for f in request.FILES.getlist('document'):
        #     print(str(f))
        uploadedFile = request.FILES['document']
        # print(uploadedFile.name)
        # print(uploadedFile.size)
        fs = FileSystemStorage()
        name = fs.save('test', uploadedFile)
        # context['nom']= uploadedFile.name
        # print(url)
        # context['url']=fs.url(name)
    return render(request,'uploadQuizz.html', context)