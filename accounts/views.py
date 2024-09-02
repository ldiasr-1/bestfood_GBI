from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UsarioForm
from django.contrib.auth.models import Group
# Create your views here.

def createuser(request):
    if request.method == "POST":
        form = UsarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Lógica para determinar o grupo do usuário
            if 'cliente' in request.POST:
                group = Group.objects.get(id=2)  # Grupo clientes
            else:
                group = Group.objects.get(id=1)  # Grupo vendedores
            user.save()
            user.groups.add(group)
            user.save_m2m()
            return HttpResponse('Usuário criado com sucesso')
        else:
            return render(request, "accounts/create.html", {"form": form})
    else:
        form = UsarioForm()
        return render(request, "accounts/create.html", {"form": form})