from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from .models import Promocao
from .forms import PromocaoForm

class PromocaoListView(LoginRequiredMixin, ListView):
    model = Promocao
    template_name = 'promo/listar_promocao.html'
    context_object_name = 'promocoes'

    def get_queryset(self):
        return Promocao.objects.all()

class PromocaoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Promocao
    form_class = PromocaoForm
    template_name = 'promo/criar_promocao.html'
    success_url = reverse_lazy('promo:listar_promocoes')
    permission_required = 'promo.add_promocao'
    raise_exception = True

    def form_valid(self, form):
        return super().form_valid(form)

class PromocaoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Promocao
    template_name = 'promo/cancelar_promocao.html'
    success_url = reverse_lazy('promo:listar_promocoes')
    permission_required = 'promo.delete_promocao'
    raise_exception = True

@login_required
@permission_required('promo.delete_promocao', raise_exception=True)
def cancelar_promocao(request, pk):
    promocao = get_object_or_404(Promocao, pk=pk)
    if request.method == 'POST':
        promocao.delete()
        return redirect('promo:listar_promocoes')
    return render(request, 'promo/cancelar_promocao.html', {'promocao': promocao})

from rest_framework import viewsets
from .models import Promocao
from .serializers import PromocaoSerializer

class PromocaoViewSet(viewsets.ModelViewSet):
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer