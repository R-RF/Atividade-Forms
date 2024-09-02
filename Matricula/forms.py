from django import forms
from Matricula.models import Aluno

class AlunoForm(forms.ModelForm):
    nome = forms.CharField(label='Nome', max_length=100)
    endereco = forms.CharField(label='Endereço', max_length=100)
    cidade = forms.CharField(label='Cidade', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    curso = forms.CharField(label='Curso', max_length=100)
    
    class Meta:
        model=Aluno
        fields= '__all__' 