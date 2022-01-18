from django.http import HttpResponse

def index(request):
    return HttpResponse('''<h1>Harry</h1> <a href="https://www.google.com">Google</a>''')

def yt(request):
    return HttpResponse('''<h1>Harry</h1> <a href="https://www.youtube.com/watch?v=JntiV4oAEOY">What If Intro Theme</a>''')

def fb(request):
    return HttpResponse('''<h1>Harry</h1> <a href="https://www.facebook.com/">Facebook</a>''')

def instagram(request):
    return HttpResponse('''<h1>Harry</h1> <a href="https://www.instagram.com/">instagram</a>''')

def bootstrap(request):
    return HttpResponse('''<h1>Harry</h1> <a href="https://getbootstrap.com/docs/5.1/forms/form-control/">Bootstrap</a>''')