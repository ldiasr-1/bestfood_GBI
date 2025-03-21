from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Produto, Tag
from .forms import ProdutoForm, TagForm
from promo.models import Promocao

# View baseada em classe para listar produtos
class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/listar_produtos.html'
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

# View baseada em classe para detalhes do produto
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produtos/produt_detail.html'
    context_object_name = 'produto'

# View baseada em função para listar produtos
def listar_produtos(request):
    query = request.GET.get('q')
    ordenar_por = request.GET.get('ordenar', 'preco')

    produtos = Produto.objects.all()

    if query:
        produtos = produtos.filter(nome__icontains=query)

    if ordenar_por == 'preco':
        produtos = produtos.order_by('preco')

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

# View baseada em função para adicionar produto
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/adicionar_produto.html', {'form': form})

# View baseada em função para editar produto
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos:produt_detail', pk=pk)
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar_produto.html', {'form': form})

# View baseada em função para deletar produto
def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('produtos:listar_produtos')
    return render(request, 'produtos/deletar_produtos.html', {'produto': produto})

# Views para tags
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