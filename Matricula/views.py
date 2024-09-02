from django.shortcuts import render
from .forms import AlunoForm    
from .models import Aluno

# Create your views here.

def cadastro_aluno(request):
     form = AlunoForm()  
     if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
            pass  
     else:
        form = AlunoForm()

     context = {
        'form': form
    }
     return render(request, 'Matricula/forms.html', context)