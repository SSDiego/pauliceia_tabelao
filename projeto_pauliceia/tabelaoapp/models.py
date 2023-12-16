from django.db import models

# Create your models here.

class form_table(models.Model):
    """
    logradouro = models.CharField(max_length=200)
    livro_emplacamento = models.CharField(max_length=1000)
    responsavel = models.CharField(max_length=200)
    dt_realizacao = models.CharField(max_length=200)
    observacao = models.CharField(max_length=1000)

    def __str__(self): 
        return self.index
    """
    id_da_rua = models.CharField(max_length=200, default='teste')
    id_ponto = models.CharField(max_length=200, default='teste')
    metragem = models.CharField(max_length=200, default='teste')
    logradouro = models.CharField(max_length=200, default='teste')
    numero = models.CharField(max_length=200, default='teste')
    numero_original = models.CharField(max_length=200, default='teste')
    data_inicial = models.CharField(max_length=200, default='2023-01-01')
    data_final = models.CharField(max_length=200, default='2023-01-01')
    fonte = models.CharField(max_length=200, default='teste')
    autor_da_alimentacao = models.CharField(max_length=200, default='teste')
    data = models.CharField(max_length=200, default='teste')
    def __str__(self): 
        return self.index
    
class MyModel(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)
    # Add more fields as needed

    def __str__(self):
        return f"{self.field1} - {self.field2}"
