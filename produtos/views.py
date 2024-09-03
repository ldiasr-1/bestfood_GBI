from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Produto, Tag
from .forms import ProdutoForm

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/listar_produtos.html'
    context_object_name = 'produtos'
    paginate_by = 10

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produtos/produt_detail.html'
    context_object_name = 'produto'

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/adicionar_produto.html', {'form': form})

def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos:produt_detail', pk=pk)  # Certifique-se de que está redirecionando para a URL correta
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar_produto.html', {'form': form})

def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('produtos:listar_produtos')
    return render(request, 'produtos/deletar_produtos.html', {'produto': produto})

def listar_tags(request):
    tags = Tag.objects.all()
    return render(request, 'produtos/listar_tags.html', {'tags': tags})
