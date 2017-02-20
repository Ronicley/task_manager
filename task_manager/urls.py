"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from task.views import *


def home(request):
    return HttpResponse("<center><h1>Olá caraio</h1></center>")
def Sobre(request):
    return HttpResponse("<center><h1>Ronicley</h1></center>")
def tarefa(request, ano,mes):
    return HttpResponse("<center><br><br><br><br>"+"<h1>tarefa: </h1>"+"<h1>"+str(ano)+"/"+str(mes)+"</h1>"+"</br></br></br></center>")
urlpatterns = [
    url(r'^home/', home),
    url(r'^Sobre/', Sobre),
    #url(r'^tarefa/([0-9]{4})/', tarefa),
    url(r'^tarefa/(?P<ano>[0-9]{4})/(?P<mes>[0-9]{2})/', tarefa),
]
