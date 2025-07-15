from django import forms
from .models import Pessoa, Candidatura

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'cpf', 'data_nasc', 'email', 'area_atuacao', 'ocupacao']
        widgets = {
            'data_nasc': forms.DateInput(attrs={'type': 'date'}),
        }

class CandidaturaForm(forms.ModelForm):
    class Meta:
        model = Candidatura
        fields = ['status']  # você pode deixar o status padrão oculto, se quiser
        widgets = {
            'status': forms.HiddenInput()
        }
