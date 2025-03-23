from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Produto, Tag
from .forms import ProdutoForm, TagForm
from promo.models import Promocao

# Views existentes (para templates HTML)
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

@login_required
@permission_required('produtos.add_produto', raise_exception=True)
def adicionar_produto(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/adicionar_produto.html', {'form': form})

@login_required
@permission_required('produtos.change_produto', raise_exception=True)
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produtos:produto_detail', pk=pk)
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar_produto.html', {'form': form})

@login_required
@permission_required('produtos.delete_produto', raise_exception=True)
def deletar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == "POST":
        produto.delete()
        return redirect('produtos:listar_produtos')
    return render(request, 'produtos/deletar_produto.html', {'produto': produto})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'produtos/tag_list.html', {'tags': tags})

@login_required
@permission_required('produtos.add_tag', raise_exception=True)
def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produtos:tag_list')
    else:
        form = TagForm()
    return render(request, 'produtos/tag_form.html', {'form': form})

@login_required
@permission_required('produtos.change_tag', raise_exception=True)
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

@login_required
@permission_required('produtos.delete_tag', raise_exception=True)
def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('produtos:tag_list')
    return render(request, 'produtos/tag_confirm_delete.html', {'tag': tag})

# Views da API
from rest_framework import viewsets
from .models import Produto, Tag
from .serializers import ProdutoSerializer, TagSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer