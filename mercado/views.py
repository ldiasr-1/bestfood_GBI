from django.shortcuts import render

# Create your views here.
# mercado/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Mercado
from .forms import MercadoForm

def listar_mercados(request):
    mercados = Mercado.objects.all()
    return render(request, 'mercado/listar_mercados.html', {'mercados': mercados})

def criar_mercado(request):
    if request.method == 'POST':
        form = MercadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mercado:listar_mercados')
    else:
        form = MercadoForm()
    return render(request, 'mercado/criar_mercado.html', {'form': form})

def editar_mercado(request, pk):
    mercado = get_object_or_404(Mercado, pk=pk)
    if request.method == 'POST':
        form = MercadoForm(request.POST, instance=mercado)
        if form.is_valid():
            form.save()
            return redirect('mercado/mercado:listar_mercados')
    else:
        form = MercadoForm(instance=mercado)
    return render(request, 'mercado/editar_mercado.html', {'form': form})

def deletar_mercado(request, pk):
    mercado = get_object_or_404(Mercado, pk=pk)
    if request.method == 'POST':
        mercado.delete()
        return redirect('mercado:listar_mercados')
    return render(request, 'mercado/deletar_mercado.html', {'mercado': mercado})
