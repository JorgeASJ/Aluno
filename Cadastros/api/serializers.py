from rest_framework import serializers
from Cadastros import models

class AlunoviewsetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aluno
        fields = '__all__'
        
class TreinoviewsetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Treino
        fields = '__all__'

class ExercicioviewsetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exercicio
        fields = '__all__'

class GrupoMuscularviewsetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GrupoMuscular
        fields = '__all__'

class TreinoAlunoviewsetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TreinoAluno
        fields = '__all__'