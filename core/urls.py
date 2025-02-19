from django.urls import path
from .views import detalhes_produto

from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:id>', produto, name='produto'),
    path('produto/<int:produto_id>/', detalhes_produto, name='detalhes_produto'),
]