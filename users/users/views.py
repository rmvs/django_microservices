from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('users')

def index(request):
    return HttpResponse('index')