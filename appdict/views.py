from django.http import HttpResponse
from django.shortcuts import render

from .models import Termo

def index(request):
   return HttpResponse("Hello, world. You're at the application index.")

def terms_list(request):
   terms = Termo.objects.order_by("termo")[:20]
   return render(request, "terms_list.html", {"terms": terms})   


def consulta_termo(request):
    descricao = None
    if request.method == 'POST':
        nome_pesquisado = request.POST.get('nome_pesquisado')
        try:
            item = Termo.objects.get(termo=nome_pesquisado)
            descricao = item.descricao
        except Termo.DoesNotExist:
            descricao = "Item não encontrado."
        except Termo.MultipleObjectsReturned:
            descricao = "Múltiplos itens encontrados com esse nome (erro no banco de dados)."

    return render(request, 'consulta_termo.html', {'descricao': descricao})
