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
    data_execucao = models.DateTimeField(auto_now=True)
    tipo_servico = models.ForeignKey(TipoServico,on_delete=models.PROTECT)
    ambiente = models.ForeignKey('entidades.Ambiente', on_delete=models.PROTECT)
    finalizado = models.BooleanField()

    def __str__(self):
        return 'Serviço: {}. Ambiente: {}'.format(self.tipo_servico.descricao,self.ambiente.descricao)


class CadastroItemChecklist(models.Model):
    OPTIONS = [
        ('BOO','BOOLEAN'),
    ]
    tipo_item = models.CharField(max_length=3,choices=OPTIONS)
    descricao = models.CharField(max_length=255)
    obrigatorio = models.BooleanField()
    publicado = models.BooleanField()

    def __str__(self):
        return self.descricao

class CadastroChecklist(models.Model):
    descricao = models.CharField(max_length=255)
    tipo_servico = models.ForeignKey(TipoServico, on_delete=models.CASCADE)
    itens = models.ManyToManyField(CadastroItemChecklist)

    def __str__(self):
        return self.descricao


class Checklist(models.Model):
    inicio_checklist = models.DateTimeField()
    ambiente = models.ForeignKey('entidades.Ambiente',on_delete=models.PROTECT)
    servico = models.ForeignKey(Servico,on_delete=models.PROTECT)
    checklist = models.ForeignKey(CadastroChecklist,on_delete=models.PROTECT)
    item = models.ForeignKey(CadastroItemChecklist, on_delete=models.PROTECT)
    valor_item = models.BooleanField(blank=True)
    imagem = models.ImageField(blank=True)
    observacao = models.TextField(blank=True)
    fim_checklist = models.DateTimeField()

    def item_value(self):
        descricao_item = ''
        if self.valor_item:
            descricao_item = 'REALIZADO'
        else:
            descricao_item = 'NÃO REALIZADO'

        return descricao_item


    def __str__(self):
        return 'Checklist: {} Item: {} Valor: {} Ambiente: {} Servico: {}'.format(self.id,self.item,self.item_value(),self.ambiente,self.servico)


















