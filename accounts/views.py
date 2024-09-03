from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.db import IntegrityError
from .forms import UsarioForm
from usuarios.models import Cliente, Vendedor

def createuser(request):
    if request.method == "POST":
        form = UsarioForm(request.POST)
        if form.is_valid():
            try:
                # Lógica para determinar o grupo do usuário e definir o username
                if form.cleaned_data.get('cpf'):
                    username = form.cleaned_data['cpf']
                    group = Group.objects.get(id=1)  # Grupo clientes
                    user = Cliente.objects.create(
                        username=username,
                        password=form.cleaned_data['password1'],
                        endereco=form.cleaned_data.get('endereco', ''),
                        telefone=form.cleaned_data.get('telefone', ''),
                        cpf=form.cleaned_data['cpf'],
                        nome=form.cleaned_data.get('nome', ''),
                        sobrenome=form.cleaned_data.get('sobrenome', ''),
                        email=form.cleaned_data.get('email', '')
                    )
                elif form.cleaned_data.get('cnpj'):
                    username = form.cleaned_data['cnpj']
                    group = Group.objects.get(id=2)  # Grupo vendedores
                    user = Vendedor.objects.create(
                        username=username,
                        password=form.cleaned_data['password1'],
                        endereco=form.cleaned_data.get('endereco', ''),
                        telefone=form.cleaned_data.get('telefone', ''),
                        cnpj=form.cleaned_data['cnpj'],
                        nome=form.cleaned_data.get('nome', ''),
                        sobrenome=form.cleaned_data.get('sobrenome', ''),
                        email=form.cleaned_data.get('email', '')
                    )
                else:
                    return HttpResponse('Erro: CPF ou CNPJ não fornecido', status=400)
                user.groups.add(group)
                return HttpResponse('Usuário criado com sucesso')
            except IntegrityError:
                return HttpResponse('Erro: CPF ou CNPJ já cadastrado', status=400)
        else:
            return redirect('add')  # Redireciona para a página add se o formulário não for válido
    else:
        form = UsarioForm()
        return render(request, 'accounts/create.html', {'form': form})