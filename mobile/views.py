from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def samsung(request):
    return HttpResponse('<h1>samsung is my Mobile </h1>')
