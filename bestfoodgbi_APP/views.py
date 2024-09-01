from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')


def obter_dados(request):
    response = requests.get('http://localhost:3000/obter_dados')  # URL do serviço Node.js
    return JsonResponse(response.json())