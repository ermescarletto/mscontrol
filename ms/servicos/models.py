from django.db import models

class TipoServico(models.Model):
    UNIDADES = [
        ('UN', 'UNIDADE'),
        ('HR', 'HORA'),
        ('MT', 'METROS'),
        ('M2', 'METRO QUADRADO'),
    ]

    RISCO = [
        ('A', 'ALTO'),
        ('M', 'MÉDIO'),
        ('B', 'BAIXO'),
    ]

    descricao = models.CharField(max_length=255)

    unidade = models.CharField(choices=UNIDADES,max_length=2)

    risco = models.CharField(choices=RISCO,max_length=1)

    observacao = models.TextField()

    tipo_ambiente = models.ManyToManyField('entidades.TipoAmbiente')

    def __str__(self):
        return self.descricao


class Servico(models.Model):

    data_execucao = models.DateField()

    tipo_servico = models.ForeignKey(TipoServico,on_delete=models.PROTECT)

    ambiente = models.ForeignKey('entidades.Ambiente', on_delete=models.PROTECT)

    entidade = models.ForeignKey('entidades.Entidade',on_delete=models.PROTECT)

    finalizado = models.BooleanField()

    def __str__(self):
        return 'Serviço: {}. Entidade: {}. Ambiente: {}'.format(self.tipo_servico.descricao,self.entidade.nome_razao,self.ambiente.descricao)


class CadastroChecklist(models.Model):

    descricao = models.CharField(max_length=255)

    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)










