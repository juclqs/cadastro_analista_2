from django import forms
from .models import Usuario, Cidade, Estado, Campus, GrupoTrabalho, Edital, GrupoAtendimento


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'chave_pix': forms.TextInput(attrs={'class': 'form-control'}),
            'campus': forms.Select(attrs={'class': 'form-select'}),
            'grupos': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'banco': forms.TextInput(attrs={'class': 'form-control'}),
            'agencia': forms.TextInput(attrs={'class': 'form-control'}),
            'conta': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-select'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome', 'estado']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }


class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['nome', 'sigla']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['nome', 'cidade', 'sigla']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.Select(attrs={'class': 'form-select'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
        }


class GrupoTrabalhoForm(forms.ModelForm):
    class Meta:
        model = GrupoTrabalho
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EditalForm(forms.ModelForm):
    class Meta:
        model = Edital
        fields = ['nome', 'numero', 'campus',
                  'avaliadores_historico', 'avaliadores_renda',
                  'data_inicial_analise_historico', 'data_final_analise_historico',
                  'data_recurso_historico', 'data_final_recurso_historico', 'data_inicial_analise_renda',
                  'data_final_analise_renda', 'data_recurso_renda',]
        widgets = {
            'campus': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'data_inicial_analise_historico': forms.DateInput(attrs={'type': 'date'}),
            'data_final_analise_historico': forms.DateInput(attrs={'type': 'date'}),
            'data_recurso_historico': forms.DateInput(attrs={'type': 'date'}),
            'data_final_recurso_historico': forms.DateInput(attrs={'type': 'date'}),
            'data_inicial_analise_renda': forms.DateInput(attrs={'type': 'date'}),
            'data_final_analise_renda': forms.DateInput(attrs={'type': 'date'}),
            'data_recurso_renda': forms.DateInput(attrs={'type': 'date'}),
            'data_final_recurso_renda': forms.DateInput(attrs={'type': 'date'}),
        }


class GrupoAtendimentoForm(forms.ModelForm):
    class Meta:
        model = GrupoAtendimento
        fields = ['nome']
