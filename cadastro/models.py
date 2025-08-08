from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.estado.sigla}"


class Campus(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    sigla = models.CharField(max_length=5)

    def __str__(self):
        return self.nome


class GrupoTrabalho(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    matricula = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, null=True, blank=True)
    endereco = models.CharField(max_length=200)
    chave_pix = models.CharField(max_length=100, null=True, blank=True)
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True)
    grupos = models.ManyToManyField(GrupoTrabalho, blank=True, null=True)
    banco = models.CharField(max_length=20)
    agencia = models.CharField(max_length=20)
    conta = models.CharField(max_length=20)
    bairro = models.CharField(max_length=30)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    cep = models.CharField(max_length=8)
    telefone = models.CharField(max_length=11)
    data_criacao = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    data_atualizacao = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    ativo = models.BooleanField(default=True, null=True, blank=True)
    recebeu_email = models.BooleanField(default=False, null=True, blank=True)
    observacoes = models.TextField(max_length=200, null=True, blank=True)

    def clean(self):
        self.cpf = ''.join(filter(str.isdigit, self.cpf))
        self.cep = ''.join(filter(str.isdigit, self.cep))
        self.telefone = ''.join(filter(str.isdigit, self.telefone))

    def __str__(self):
        return self.nome


class Edital(models.Model):
    nome = models.CharField(max_length=200)
    numero = models.CharField(max_length=50)
    campus = models.ManyToManyField(Campus, blank=True)
    avaliadores_historico = models.ManyToManyField(
        Usuario, blank=True, related_name='editais_historico')
    avaliadores_renda = models.ManyToManyField(
        Usuario, blank=True, related_name='editais_renda')
    data_inicial_analise_historico = models.DateField(null=True, blank=True)
    data_final_analise_historico = models.DateField(null=True, blank=True)
    data_recurso_historico = models.DateField(null=True, blank=True)
    data_final_recurso_historico = models.DateField(null=True, blank=True)
    data_inicial_analise_renda = models.DateField(null=True, blank=True)
    data_final_analise_renda = models.DateField(null=True, blank=True)
    data_recurso_renda = models.DateField(null=True, blank=True)
    data_final_recurso_renda = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True, null=True, blank=True)
    data_criacao = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    data_atualizacao = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    observacoes = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.numero})"


class GrupoAtendimento(models.Model):
    nome = models.CharField(max_length=200)
    edital = models.ForeignKey(
        Edital, on_delete=models.CASCADE, related_name='grupos')

    def __str__(self):
        return self.nome
