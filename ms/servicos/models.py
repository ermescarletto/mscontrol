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




class ChecklistPreenchido(models.Model):
    foto_checklist_antes = models.ImageField(blank=True)
    ambiente = models.ForeignKey('entidades.Ambiente',on_delete=models.PROTECT)
    checklist = models.ForeignKey(CadastroChecklist,on_delete=models.PROTECT)
    itens = models.JSONField()
    foto_checklist_depois = models.ImageField(blank=True)
    data_hora = models.DateTimeField(auto_now=True, auto_created=True)

    def __str__(self):
        return 'Checklist: {}'.format(str(self.checklist))












