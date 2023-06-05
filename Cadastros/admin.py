from django.contrib import admin

# Register your models here.

from .models import Aluno, Treino, TreinoAluno, Exercicio, GrupoMuscular

admin.site.register(Aluno)
admin.site.register(Treino)
admin.site.register(TreinoAluno)
admin.site.register(Exercicio)
admin.site.register(GrupoMuscular)