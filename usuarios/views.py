from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Cliente, Vendedor
from .forms import ClienteForm, VendedorForm

# Views existentes (para templates HTML)
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'usuarios/listar_clientes.html', {'clientes': clientes})

@login_required
@permission_required('usuarios.add_cliente', raise_exception=True)
def criar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_clientes')
    else:
        form = ClienteForm()
    return render(request, 'usuarios/criar_cliente.html', {'form': form})

@login_required
@permission_required('usuarios.change_cliente', raise_exception=True)
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('usuarios:listar_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'usuarios/editar_cliente.html', {'form': form})

@login_required
@permission_required('usuarios.delete_cliente', raise_exception=True)
def deletar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('usuarios:listar_clientes')
    return render(request, 'usuarios/deletar_cliente.html', {'cliente': cliente})

def listar_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'usuarios