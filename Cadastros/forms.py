from django import forms
from Cadastros.models import Aluno
from datetime import datetime

class AlunoForm(forms.ModelForm):
    Nome = forms.CharField(max_length=20)
    Senha = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput)
    Idade = forms.IntegerField()
    Peso = forms.FloatField()
    Altura = forms.FloatField()
    Contato = forms.CharField()
    Objetivo = forms.CharField()
    dt_vencimentoPlano = forms.DateField(widget=forms.DateInput(attrs={'type':'date','min':datetime.now().date()}))
    fl_ativo = forms.BooleanField(required=False)
    class Meta:
        model = Aluno
        exclude = ()
        