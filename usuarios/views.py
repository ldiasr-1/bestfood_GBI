from django.shortcuts import render, get_object_or_404
from .forms import PessoaForm, UsuarioUpdateForm
from .models import Pessoa
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required
def index(request):
    return render(request, "pessoa/index.html")

@login_required
def create(request):
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pessoa/list/')
    else:
        form = PessoaForm()
    return render(request, "pessoa/add.html", {"form": form})

@login_required
def read(request):
    filtro = {}
    for key, value in request.GET.items():
        if key in ['cpf', 'telefone', 'nome', 'endereco']:
            filtro[f"{key}__icontains"] = value

    pessoas = Pessoa.objects.filter(**filtro)
    return render(request, "pessoa/list.html", {"pessoas": pessoas})

@login_required
def update(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, pk=pessoa_id)
    if request.method == "POST":
        form = UsuarioUpdateForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pessoa/list/')
    else:
        form = UsuarioUpdateForm(instance=pessoa)
    return render(request, 'pessoa/edit.html', {'form': form})

@login_required
def delete(request, pessoa_id):
    Pessoa.objects.get(pk=pessoa_id).delete()
    return HttpResponseRedirect("/pessoa/list/")

@login_required
def detail(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, pk=pessoa_id)
    return render(request, "pessoa/detail.html", {"pessoa": pessoa})

from rest_framework import viewsets
from .models import Cliente, Vendedor
from .serializers import ClienteSerializer, VendedorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer