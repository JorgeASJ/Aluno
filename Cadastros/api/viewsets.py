from rest_framework import viewsets
from Cadastros.api import serializers
from Cadastros import models

class Alunoviewsets(viewsets.ModelViewSet):
    serializer_class = serializers.AlunoviewsetsSerializer
    queryset = models.Aluno.objects.all()

class Treinoviewsets(viewsets.ModelViewSet):
    serializer_class = serializers.TreinoviewsetsSerializer
    queryset = models.Treino.objects.all()

class Exercicioviewsets(viewsets.ModelViewSet):
    serializer_class = serializers.ExercicioviewsetsSerializer
    queryset = models.Exercicio.objects.all()

class GrupoMuscularviewsets(viewsets.ModelViewSet):
    serializer_class = serializers.GrupoMuscularviewsetsSerializer
    queryset = models.GrupoMuscular.objects.all()

class TreinoAlunoviewsets(viewsets.ModelViewSet):
    serializer_class = serializers.TreinoAlunoviewsetsSerializer
    queryset = models.TreinoAluno.objects.all()