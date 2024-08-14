from django.shortcuts import render
from app.forms import *
from django.http import *

# Create your views here.

def insert_topic(request):
    ETFO=TopicModelForm()
    d={"ETFO":ETFO}
    if request.method=='POST':
        TFDO=TopicModelForm(request.POST)
        TFDO.save()
        return HttpResponse("Topic is created")
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageModelForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageModelForm(request.POST)
        WFDO.save()
        return HttpResponse('Webpage is created')
    return render(request,"insert_webpage.html",d)

def insert_accessrecord(request):
    EAFO=AccessRecordModelForm()
    d={"EAFO":EAFO}
    if request.method=='POST':
        AFDO=AccessRecordModelForm(request.POST)
        AFDO.save()
        return HttpResponse('AccessRecord is created')
    return render(request,'insert_accessrecord.html',d)