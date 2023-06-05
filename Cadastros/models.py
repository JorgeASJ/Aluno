from django.db import models
from uuid import uuid4

# Create your models here.
class Aluno(models.Model):
    #id_Aluno = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_Aluno = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=255)
    Senha = models.CharField(max_length=255)
    Idade = models.IntegerField()
    Peso = models.FloatField()
    Altura = models.FloatField()
    Contato = models.CharField(max_length=255)
    Objetivo = models.CharField(max_length=255)
    dt_Cadasto = models.DateField(auto_now_add=True)
    dt_vencimentoPlano = models.DateField(null=True)
    fl_ativo = models.BooleanField()

    def __str__(self) -> str:
        return self.Nome

class Treino(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.Nome

class GrupoMuscular(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.Nome


class Exercicio(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    id_GrupoMuscular = models.ForeignKey(GrupoMuscular, on_delete=models.CASCADE)
    Nome = models.CharField(max_length=255)
    link = models.CharField(max_length=255,blank=True)
    def __str__(self) -> str:
        return self.Nome

class TreinoAluno(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    id_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    id_Treino = models.ForeignKey(Treino, on_delete=models.DO_NOTHING)
    id_GrupoMuscular = models.ForeignKey(GrupoMuscular, on_delete=models.DO_NOTHING)
    id_Excecicio = models.ForeignKey(Exercicio, on_delete=models.DO_NOTHING)
    qt_series =  models.IntegerField()
    qt_repeticoes = models.IntegerField()
    qt_peso = models.IntegerField()
    dt_expiracao = models.DateField(null=True)
    def __str__(self) -> str:
        return self.Nome
