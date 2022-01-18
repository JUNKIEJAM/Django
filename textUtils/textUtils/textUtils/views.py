#I have created this file
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>hello</h1>")

def about(request):
    return HttpResponse("<h1>About me</h1>")
