from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Produto, Tag
from .forms import ProdutoForm, TagForm
from django.db.models import Min
from promo.models import Promocao
from promo.forms import PromocaoForm
from produtos.models import Produto

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
    query = request.GET.get('q')
    ordenar_por = request.GET.get('ordenar', 'preco')

    produtos = Produto.objects.all()

    if query:
        produtos = produtos.filter(nome__icontains=query)

    if ordenar_por == 'preco':
        produtos = produtos.order_by('preco')

    # Adicionar valor promocional
    produtos_com_promocao = []
    for produto in produtos:
        promocao = Promocao.objects.filter(produtos=produto).first()
        if promocao:
            preco_promocional = produto.preco * (1 - promocao.percentual / 100)
        else:
            preco_promocional = produto.preco
        produtos_com_promocao.append({
            'produto': produto,
            'preco_promocional': preco_promocional
        })

    return render(request, 'produtos/listar_produtos.html', {'produtos_com_promocao': produtos_com_promocao, 'query': query, 'ordenar_por': ordenar_por})

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


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produt_list.html'
    context_object_name = 'produtos'
    paginate_by = 10

def get_queryset(self):
    ordenar_por = self.request.GET.get('ordenar', 'preco')
    queryset = Produto.objects.all().distinct()

    if ordenar_por == 'preco':
        queryset = queryset.order_by('preco')
    elif ordenar_por == 'nome':
        queryset = queryset.order_by('nome')
    return queryset
    

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'produtos/tag_list.html', {'tags': tags})

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:tag_list')
    else:
        form = TagForm()
    return render(request, 'produtos/tag_form.html', {'form': form})

def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect('produtos:tag_list')
    else:
        form = TagForm(instance=tag)
    return render(request, 'produtos/tag_form.html', {'form': form})

def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('produtos:tag_list')
    return render(request, 'produtos/tag_confirm_delete.html', {'tag': tag})
