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
    endereco = models.CharField(max_length=200, blank=True, null=True)
    chave_pix = models.CharField(max_length=100, null=True, blank=True)
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True)
    grupos = models.ManyToManyField(GrupoTrabalho, blank=True, null=True)
    banco = models.CharField(max_length=30, blank=True, null=True)
    agencia = models.CharField(max_length=20, blank=True, null=True)
    conta = models.CharField(max_length=20, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_criacao = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    data_atualizacao = models.DateTimeField(
        auto_now=True, null=True, blank=True)
    ativo = models.BooleanField(default=True, null=True, blank=True)
    recebeu_email = models.BooleanField(default=False, null=True, blank=True)
    observacoes = models.TextField(max_length=200, null=True, blank=True)

    def clean(self):
        super().clean()

        if self.cpf:
            self.cpf = ''.join(filter(str.isdigit, str(self.cpf)))

        if self.cep:
            self.cep = ''.join(filter(str.isdigit, str(self.cep)))

        if self.telefone:
            self.telefone = ''.join(filter(str.isdigit, str(self.telefone)))

    def __str__(self):
        return self.nome


class Edital(models.Model):
    nome = models.CharField(max_length=200)
    numero = models.CharField(max_length=50)
    ano = models.CharField(max_length=4, null=True, blank=True)
    campus = models.ManyToManyField(Campus, blank=True)
    avaliadores_historico = models.ManyToManyField(
        Usuario, blank=True, related_name='editais_historico')
    avaliadores_renda = models.ManyToManyField(
        Usuario, blank=True, related_name='editais_renda')
    valor_unitario_avaliacao = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    valor_unitario_renda = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
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


class Avaliacao(models.Model):
    avaliador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    edital = models.ForeignKey(Edital, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=[(
        "analise", "Análise"), ("recurso", "Recurso")])
