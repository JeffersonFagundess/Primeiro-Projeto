from django.db import models

class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('preco', decimal_places=2, max_digits=8)
    descricao = models.TextField(null=True, blank=True)
    estoque = models.IntegerField('Quantidade em estoque')
    imagem = models.ImageField('imagem', upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    email = models.EmailField('email', max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome} - {self.email}'
