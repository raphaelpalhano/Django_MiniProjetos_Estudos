from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(requests):
    return render(requests, "hello/index.html")


def Mensage(requests):
    return HttpResponse("Se eu cair vou me levantar! Se alguém me derrubar eu vou me levantar!")

def Named(requests, name):
    return render(requests, "hello/greet.html", {
        "name": name.capitalize()
    })