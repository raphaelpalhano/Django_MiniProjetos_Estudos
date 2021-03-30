from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse



# objeto de formulário, contendo o input text, e priority.
class NewTaskForm(forms.Form):
    # definir os campos que o formulário terá como entrada:
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10) # definindo o limite de quanto o usuário poderá digitar

# Página inicial que vai mostrar a lista de tarefas
def index(request):
    # verifique se as tarefas não estão a requisição:
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "mytask/index.html", {
        "tasks": request.session["tasks"]
    })

# função que vai ter o processo de verificar de formulário e a rota da página de formulário para adicionar tarefas
def add(request):
    #verificando se o método é o post
    if request.method == "POST":
        # se o usuário tiver enviado alguns dados crie a variável:
        form = NewTaskForm(request.POST)
        # verificando se as informações são válidas
        if form.is_valid():
            task =form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            # caso esse formulário não for válido, retorne para add.html novamente!
            return render(request, "tasks/add.html", {
                "form": form #irá gerar a informação dos erros cometidos.
            })
    # if method != "POST": vai obter a página para exbir o conteúdo.
    return render(request, "mytask/add.html", {
        "form": NewTaskForm()
    })
