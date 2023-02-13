from django.db import models

# Create your models here.
class Hub(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class GrupoVeiculo(models.Model):
    descricao = models.CharField(max_length=100)
    valor_diaria = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.descricao

class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=7)
    grupo = models.ForeignKey(GrupoVeiculo, on_delete=models.CASCADE, related_name="veiculos", default=None)

    def __str__(self):
        return self.modelo
