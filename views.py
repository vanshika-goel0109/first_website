from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def removepunc(request):
    djtext=request.GET.get('text','default')
    print(djtext)
    return HttpResponse("removepunc")
