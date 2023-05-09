from django.db import models


class SearchCOOLERS(models.Model):
    marca = models.CharField(max_length=100)
    url_marca = models.CharField(max_length=100)
    loja = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    valor_preco_prazo = models.DecimalField(
        max_digits=7, decimal_places=2, null=True)
    preco_antigo = models.DecimalField(
        max_digits=7, decimal_places=2, null=True)
    ativo = models.DecimalField(
        max_digits=7, decimal_places=2, default=0, null=True)

    def __str__(self):
        return self.marca + " "
