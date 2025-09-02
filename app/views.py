from django.shortcuts import render
from .models import *
from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .forms import PessoaForm, CandidaturaForm
from datetime import date

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

def vagas_view(request):
    vagas = Vaga.objects.all()  # Corrigido
    return render(request, 'vagas.html', {'vagas': vagas})

def empresas_view(request):
    empresas = Empresa.objects.all()  # Corrigido
    return render(request, 'empresas.html', {'empresas': empresas})

def dicas_view(request):
    return render(request, 'dicas.html')


def candidatar_view(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)

    if request.method == 'POST':
        pessoa_form = PessoaForm(request.POST)
        if pessoa_form.is_valid():
            pessoa = pessoa_form.save()
            Candidatura.objects.create(
                pessoa=pessoa,
                vaga=vaga,
                data_candidatura=date.today(),
                status="Em análise"
            )
            return render(request, 'candidatura_sucesso.html', {'vaga': vaga})
    else:
        pessoa_form = PessoaForm()

    return render(request, 'candidatar.html', {
        'vaga': vaga,
        'form': pessoa_form
    })
# Lista todas as candidaturas
def lista_candidaturas(request):
    candidaturas = Candidatura.objects.all()
    return render(request, "candidaturas.html", {"candidaturas": candidaturas})

# Exibe os detalhes de uma candidatura
def detalhe_candidatura(request, candidatura_id):
    candidatura = get_object_or_404(Candidatura, id=candidatura_id)
    return render(request, "detalhe_candidatura.html", {"candidatura": candidatura})

# Excluir candidatura
def excluir_candidatura(request, candidatura_id):
    candidatura = get_object_or_404(Candidatura, id=candidatura_id)
    candidatura.delete()
    return redirect("lista_candidaturas")
