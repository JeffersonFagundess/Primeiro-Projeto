from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    
    context = {
        'curso': 'Programação e valor',
        'outra': 'Lista de Produtos',
        'produtos': produtos
    }
    return render(request, 'index.html', context,)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    #prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/hmtl; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/hmtl; charset=utf8', status=500)


from django.shortcuts import render

def detalhes_produto(request, produto_id):
    lista_produtos = {
        1: {"nome": "PC Gamer", "imagem": "pc_gamer.png"},
        2: {"nome": "Memória RAM", "imagem": "memoria.png"},
        3: {"nome": "Gabinete Gamer", "imagem": "gabinete.png"},
    }

    produto = lista_produtos.get(produto_id, None)

    if not produto:
        return render(request, "erro.html", {"mensagem": "Produto não encontrado"})

    return render(request, "produto.html", {"produto": produto})

