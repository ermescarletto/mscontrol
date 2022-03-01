from django.db import models

# Create your models here.
class Pais(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Paises'



class Estado(models.Model):
    nome = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    codigo_ibge = models.IntegerField()
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Logradouro(models.Model):
    TIPO_LOGRADOURO = [
        ('RUA','RUA'),
        ('AVENIDA','AVENIDA'),
        ('TRAVESSA','TRAVESSA'),
        ('ALAMEDA','ALAMEDA'),
        ('LADEIRA','LADEIRA'),
    ]
    tipo_logradouro = models.CharField(max_length=255,choices=TIPO_LOGRADOURO,default='RUA')
    nome = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome



class Pessoa(models.Model):
    TIPO_PESSOA = [
        ('F','Física'),
        ('J','Jurídica'),
        ('O','Outra')
    ]
    tipo_pessoa = models.CharField(max_length=1,choices=TIPO_PESSOA)
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    cpfcnpj = models.CharField(max_length=14)
    rg = models.PositiveIntegerField()
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)
    logradouro = models.ForeignKey(Logradouro,on_delete=models.CASCADE)
    numero = models.PositiveIntegerField()
    complemento = models.CharField(max_length=255)

    def __str__(self):
        return self.nome