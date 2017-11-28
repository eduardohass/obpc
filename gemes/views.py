from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1> This is a index page")

def detail(request, grupo_id):
    return HttpResponse("<h2>Details for Grupo do gemes by ID: " + str(grupo_id) + "</h2>")