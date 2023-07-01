from django.db import models

# Create your models here.

class form_table(models.Model):
    index = models.SmallIntegerField(default=10)
    logradouro = models.CharField(max_length=200)
    livro_emplacamento = models.CharField(max_length=200)
    responsavel = models.CharField(max_length=200)
    dt_realizacao = models.DateField()
    observacao = models.CharField(max_length=200)

    def __str__(self): 
        return self.index
