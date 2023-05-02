from django.db import models


class SearchMemory(models.Model):
    marca = models.CharField(max_length=100)
    url_marca = models.CharField(max_length=100)
    loja = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    valor_preco_prazo = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.marca + " "