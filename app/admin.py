from django.contrib import admin
from .models import Cidade, AreaAtuacao, Ocupacao, Pessoa, Empresa, Vaga, Candidatura

# Inline para Vaga dentro da Empresa
class VagaInline(admin.TabularInline):
    model = Vaga
    extra = 1

# Inline para Candidatura dentro da Pessoa
class CandidaturaPessoaInline(admin.TabularInline):
    model = Candidatura
    extra = 1

# Inline para Candidatura dentro da Vaga
class CandidaturaVagaInline(admin.TabularInline):
    model = Candidatura
    extra = 1

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')
    list_filter = ('uf',)
    search_fields = ('nome',)

@admin.register(AreaAtuacao)
class AreaAtuacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Ocupacao)
class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'data_nasc', 'email', 'area_atuacao', 'ocupacao')
    search_fields = ('nome', 'cpf', 'email')
    inlines = [CandidaturaPessoaInline]

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'setor', 'site', 'telefone', 'cidade')
    search_fields = ('nome', 'setor')
    inlines = [VagaInline]

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa', 'cidade', 'area_atuacao', 'ocupacao')
    search_fields = ('nome', 'empresa__nome', 'cidade__nome')
    inlines = [CandidaturaVagaInline]

@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'vaga', 'data_candidatura', 'status')
    search_fields = ('pessoa__nome', 'vaga__nome', 'status')
    list_filter = ('status',)

# Registrando modelos que não possuem Admin personalizado (caso tenha)
# Exemplo:
# admin.site.register(OutraModel)

