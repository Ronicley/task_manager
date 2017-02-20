from django.shortcuts import render
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
class tarefa(object):
    titulo=None
    data=None
    def __init__(self, titulo, data):
        titulo=titulo
        data=data
    def __str__(self):
        return self.titulo
def home(request):
    return HttpResponse("<center><h1>Olá caraio</h1></center>")
def Sobre(request):
    return HttpResponse("<center><h1>Ronicley</h1></center>")
def tarefa(request, ano,mes):
    return HttpResponse("<center><br><br><br><br>"+"<h1>tarefa: </h1>"+"<h1>"+str(ano)+"/"+str(mes)+"</h1>"+"</br></br></br></center>")
