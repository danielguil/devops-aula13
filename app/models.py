"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    periodo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=200)

class Vestibular(models.Model):
    nome = models.CharField(max_length=200)
    
class candidato(models.Model):
    nome = models.CharField(max_length=60)
    endereco = models.CharField(max_length=150)
    telefone = models.IntegerField(max_length=200)
    CPF = models.IntegerField(max_length=200) 
    RG = models.IntegerField(max_length=200)

