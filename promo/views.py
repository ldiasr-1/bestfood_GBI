from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView
from .models import Promocao
from .forms import PromocaoForm
from django.urls import reverse_lazy

def listar_promocoes(request):
    promocoes = Promocao.objects.all()
    return render(request, 'promo/listar_promocao.html', {'promocoes': promocoes})

class PromocaoCreateView(CreateView):
    model = Promocao
    form_class = PromocaoForm
    template_name = 'promo/criar_promocao.html'
    success_url = reverse_lazy('promo:listar_promocoes')  # Substitua pelo nome correto da URL de listagem

    def form_valid(self, form):
        # Você pode adicionar lógica extra aqui, se necessário
        return super().form_valid(form)

def cancelar_promocao(request, pk):
    promocao = get_object_or_404(Promocao, pk=pk)
    if request.method == 'POST':
        promocao.delete()
        return redirect('promo:listar_promocoes')
    else:
        # Exibir confirmação de cancelamento
        return render(request, 'promo/cancelar_promocao.html', {'promocao': promocao})


class PromocaoListView(ListView):
    model = Promocao
    template_name = 'promo/listar_promocao.html'
    context_object_name = 'promocoes'

class PromocaoCreateView(CreateView):
    model = Promocao
    form_class = PromocaoForm
    template_name = 'promo/criar_promocao.html'
    success_url = '/promo/'

class PromocaoDeleteView(DeleteView):
    model = Promocao
    template_name = 'promo/cancelar_promocao.html'
    success_url = '/promo/'

class PromocaoCreateView(CreateView):
    model = Promocao
    form_class = PromocaoForm
    template_name = 'promo/criar_promocao.html'
    success_url = reverse_lazy('promo:listar_promocoes')