from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Entidade(models.Model):
    TIPO_ENTIDADE = [
        ('G','Governo'),
        ('A','Autarquia'),
        ('P','Privada'),
        ('M','Mista')
    ]

    nome_razao = models.CharField(max_length=255,unique=True, verbose_name='Nome/Razão')
    pessoa = models.ForeignKey('cadastrounico.Pessoa',on_delete=models.PROTECT)
    tipo_entidade = models.CharField(max_length=1,choices=TIPO_ENTIDADE)

    def __str__(self):
        return self.nome_razao


class Contrato(models.Model):
    entidade = models.ForeignKey(Entidade,on_delete=models.PROTECT)
    numero = models.CharField(max_length=10)
    ano = models.CharField(max_length=4)
    data_validade = models.DateField()
    prorrogavel = models.BooleanField()
    valor_contrato = models.DecimalField(decimal_places=2,max_digits=8)
    responsavel = models.ForeignKey('cadastrounico.Pessoa',on_delete=models.PROTECT)
    observacao = models.TextField()

    def __str__(self):
        return 'Contrato: {} / {}'.format(self.numero,self.ano)

class Alas(models.Model):
    nome = models.CharField(max_length=255)
    codigo = models.CharField(max_length=8)
    entidade = models.ForeignKey(Entidade, on_delete=models.PROTECT)
    especialidade = models.CharField(max_length=255,blank=True)

class TipoAmbiente(models.Model):
    RISCO = [
        ('A','ALTO'),
        ('M','MÉDIO'),
        ('B','BAIXO'),
    ]
    descricao = models.CharField(max_length=255)
    risco = models.CharField(max_length=1,choices=RISCO)
    controla_checklist = models.BooleanField(default=True)
    checklists_relacionados = models.ManyToManyField('servicos.CadastroChecklist')
    entidade = models.ForeignKey(Entidade,on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao

class Ambiente(models.Model):
    tipo_ambiente = models.ForeignKey(TipoAmbiente,on_delete=models.PROTECT)
    descricao = models.CharField(max_length=255)
    codigo = models.CharField(max_length=20, blank=True)
    area = models.DecimalField(decimal_places=2,max_digits=8)
    andar = models.CharField(max_length=20,blank=True)
    bloco = models.CharField(max_length=20,blank=True)
    entidade = models.ForeignKey(Entidade,on_delete=models.PROTECT)
    imagem = models.ImageField(blank=True)
    def __str__(self):
        return self.descricao

class StatusAmbiente(models.Model):
    STATUS = [
        ('L', 'Liberado'),
        ('A', 'Aguardando Manutenção'),
        ('E', 'Em Manutenção'),
    ]
    ambiente = models.ForeignKey(Ambiente, on_delete=models.PROTECT)
    status = models.CharField(choices=STATUS, max_length=1)
    data_hora = models.DateTimeField(auto_created=True, auto_now=True)

    usuario = models.ForeignKey(User,on_delete=models.PROTECT)
