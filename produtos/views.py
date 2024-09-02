from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Produto
from .forms import ProdutoForm


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produt_list.html'
    context_object_name = 'produtos'
    paginate_by = 10  # Número de produtos por página

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
            return redirect('produtos:listar')  # Certifique-se de que 'produtos:listar' é um nome de URL válido
    else:
        form = ProdutoForm()
    return render(request, 'produtos/adicionar_produto.html', {'form': form})