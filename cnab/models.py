from django.db import models

# Create your models here.
from django import forms

class Importation(models.Model):
    class Meta:
        verbose_name = 'Arquivo importado'
        verbose_name_plural = 'Arquivos importados'
    name = models.CharField(max_length=50, null=True, verbose_name='Nome referente ao arquivo')
    file = models.FileField(upload_to='fil')
