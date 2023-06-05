import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Cadastros.models import Aluno
from Cadastros.forms import AlunoForm
from django.contrib import messages

# Create your views here.
# Cadastro de Alunos

def home(request):
    return HttpResponse('teste')


def alunos(request):
    alunos = {
        'alunos': Aluno.objects.all()
    }
    return render(request,'alunos.html', alunos)

def cadastroAluno(request):
    data = {}
    data['form'] = AlunoForm()
    return render(request,'cadastroAluno.html', data)

def cadastroAluno2(request):
    data = {}
    data['form'] = AlunoForm()
    return render(request,'cadastroAluno2.html', data)

def incluiAluno(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,"Usuário Cadastrado Com Sucesso!")
    return redirect('alunos')    
   
def editAluno(request, pk):
    data = {}
    data['db'] = Aluno.objects.get(pk=pk)
    data['form'] = AlunoForm(instance=data['db'])
    return render (request,'cadastroAluno.html', data)
   
def atualizaAluno(request,pk):
    data = {}
    data['db'] = Aluno.objects.get(pk=pk)
    form = AlunoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        messages.success(request,"Usuário Atualizado Com Sucesso!")
    return redirect('alunos')    

def excluiAluno(request,pk):
    db = Aluno.objects.get(pk=pk)
    db.delete()
    messages.success(request,"Usuário Excluido Com sucesso!")
    return redirect('alunos')


#cadastro de Grupo Musculares
#Cadastro de Exercicios
#Cadastro de Treinos



