from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.


def my_year(requests):
    now = datetime.datetime.now()
    return render(requests, "newyear/index.html",{
        "newyear": now.month == 1 and now.day == 1
        # se ambos forem 1 a variável será True caso contrário falso

    })
    # ROTA PARA VERIFICAR SE É PRIMEIRO DE JANEIRO YES == TRUE; NO == FALSE
    