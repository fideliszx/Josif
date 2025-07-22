from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=40)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} - {self.uf}"


class AreaAtuacao(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Áreas de Atuação'
        verbose_name_plural = 'Áreas de Atuação'


class Ocupacao(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Ocupação'
        verbose_name_plural = 'Ocupações'


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    data_nasc = models.DateField()
    email = models.EmailField(max_length=15)
    area_atuacao = models.ForeignKey(AreaAtuacao, on_delete=models.SET_NULL, null=True, blank=True)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    nome = models.CharField(max_length=40)
    setor = models.CharField(max_length=40)
    site = models.CharField(max_length=40)
    telefone = models.CharField(max_length=25)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    nome = models.CharField(max_length=40)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='vagas')
    requisitos = models.CharField(max_length=40)
    beneficios = models.CharField(max_length=40)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    area_atuacao = models.ForeignKey(AreaAtuacao, on_delete=models.SET_NULL, null=True, blank=True)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Candidatura(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    data_candidatura = models.DateField()
    status = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.pessoa.nome} - {self.vaga.nome}"
