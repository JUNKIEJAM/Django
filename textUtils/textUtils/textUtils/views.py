#I have created this file
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
 #   return HttpResponse("<h1>hello</h1>")

#def about(request):
 #   return HttpResponse("<h1>About me</h1>")

def index(request):
   # params={'name':'harry','place':'Mars'}
    return render(request,'index.html')
    #return HttpResponse("Home")

def removepunc(request):
    djtext=request.GET.get('text','default')
    print(djtext)
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("new line remove")

def spaceremove(request):
    return HttpResponse("space remove <a href='/'>back</a>" )

def charcount(request):
    return HttpResponse("char count")