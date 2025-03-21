from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.db import IntegrityError
from .forms import UsarioForm
from usuarios.models import Cliente, Vendedor

def createuser(request):
    if request.method == "POST":
        form = UsarioForm(request.POST)
        if form.is_valid():
            try:
                if form.cleaned_data.get('cpf'):
                    user = Cliente.objects.create_user(
                        username=form.cleaned_data['cpf'],
                        password=form.cleaned_data['password1'],
                        endereco=form.cleaned_data.get('endereco', ''),
                        telefone=form.cleaned_data.get('telefone', ''),
                        cpf=form.cleaned_data['cpf'],
                        nome=form.cleaned_data.get('nome', ''),
                        sobrenome=form.cleaned_data.get('sobrenome', ''),
                        email=form.cleaned_data.get('email', '')
                    )
                elif form.cleaned_data.get('cnpj'):
                    user = Vendedor.objects.create_user(
                        username=form.cleaned_data['cnpj'],
                        password=form.cleaned_data['password1'],
                        endereco=form.cleaned_data.get('endereco', ''),
                        telefone=form.cleaned_data.get('telefone', ''),
                        cnpj=form.cleaned_data['cnpj'],
                        nome=form.cleaned_data.get('nome', ''),
                        sobrenome=form.cleaned_data.get('sobrenome', ''),
                        email=form.cleaned_data.get('email', '')
                    )
                else:
                    messages.error(request, 'Erro: CPF ou CNPJ não fornecido')
                    return redirect('accounts:add')

                messages.success(request, 'Usuário criado com sucesso')
                auth_login(request, user)  # Faz login automaticamente após o cadastro
                return redirect('produtos:listar_produtos')  # Redireciona para a página inicial
            except IntegrityError as e:
                messages.error(request, f'Erro: {str(e)}')
                return redirect('accounts:add')
        else:
            messages.error(request, 'Formulário inválido')
            return redirect('accounts:add')
    else:
        form = UsarioForm()
        return render(request, 'accounts/create.html', {'form': form})