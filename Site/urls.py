from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from Cadastros.api import viewsets as cadastroViewsets
from Cadastros import views

route = routers.DefaultRouter()

route.register(r'Aluno',cadastroViewsets.Alunoviewsets, basename='Aluno')
route.register(r'Treino',cadastroViewsets.Treinoviewsets, basename='Treino')
route.register(r'Exercicio',cadastroViewsets.Exercicioviewsets, basename='Exercicio')
route.register(r'GrupoMuscular',cadastroViewsets.GrupoMuscularviewsets, basename='GrupoMuscular')
route.register(r'TreinoAluno',cadastroViewsets.TreinoAlunoviewsets, basename='TreinoAluno')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Cadastros.urls')),
    path('api/',include(route.urls), name='api'),
    path('alunos/', views.alunos,name='alunos'),
    path('cadastroAluno/', views.cadastroAluno,name='cadastroAluno'),
    path('cadastroAluno2/', views.cadastroAluno2,name='cadastroAluno2'),
    path('incluiAluno/', views.incluiAluno,name='incluiAluno'),
    path('editAluno/<int:pk>/', views.editAluno,name='editAluno'),
    path('atualizaAluno/<int:pk>/', views.atualizaAluno,name='atualizaAluno'),
    path('excluiAluno/<int:pk>/', views.excluiAluno,name='excluiAluno')
]
