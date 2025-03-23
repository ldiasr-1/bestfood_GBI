from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Promocao
from .forms import PromocaoForm

# Views existentes (para templates HTML)
def listar_promocoes(request):
    promocoes = Promocao.objects.all()
    return render(request, 'promo/listar_promocao.html', {'promocoes': promocoes})

@login_required
@permission_required('promo.add_promocao', raise_exception=True)
def criar_promocao(request):
    if request.method == 'POST':
        form = PromocaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('promo:listar_promocoes')
    else:
        form = PromocaoForm()
    return render(request, 'promo/criar_promocao.html', {'form': form})

@login_required
@permission_required('promo.delete_promocao', raise_exception=True)
def cancelar_promocao(request, pk):
    promocao = get_object_or_404(Promocao, pk=pk)
    if request.method == 'POST':
        promocao.delete()
        return redirect('promo:listar_promocoes')
    return render(request, 'promo/cancelar_promocao.html', {'promocao': promocao})

# Views da API
from rest_framework import viewsets
from .models import Promocao
from .serializers import PromocaoSerializer

class PromocaoViewSet(viewsets.ModelViewSet):
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer