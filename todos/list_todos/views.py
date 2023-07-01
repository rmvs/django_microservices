from django.http import HttpResponse
from django.shortcuts import render

def list_todos(request):
    return HttpResponse('list-todos')
