from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from datetime import date
import datetime as DT

# class Quantidade(models.Model):
#     UNIDADES = 'Unidades'
#     PACOTES = 'Pacotes'
#     LATAS = 'Latas'
#     CAIXAS = 'Caixas'
#     ESCOLHA = [(UNIDADES, 'Unidades'),
#               (PACOTES, 'Pacotes'),
#               (LATAS, 'Latas'),
#               (CAIXAS, 'Caixas'),]
#     tipo = models.CharField(
#         max_length=10,
#         choices=ESCOLHA,
#         default=UNIDADES,)

#     def __str__(self):
#         return self.tipo

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    quantidade = models.IntegerField()
    validade = models.DateField()

    CHOICES = (
        ('Un', 'Unidades'),
        ('Pc', 'Pacotes'),
        ('Lt', 'Latas'),
        ('Cx', 'Caixas'),
    )

    tipo = models.CharField(max_length=10, choices = CHOICES, default='Un')

    usuario = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        ordering = ('validade',)

    def get_absolute_url(self):
        return reverse('produto_edit', args=[self.pk])

    @property
    def is_expired(self):
        return self.validade < date.today()
    def is_close_expire(self):
        past_expire = self.validade < date.today()
        close_expire = self.validade < date.today() + DT.timedelta(days=7)
        return  not (past_expire) and close_expire

    def __str__(self):
        return self.nome

class Receita(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    descricao = models.TextField(verbose_name="Modo de Preparo")

    usuario = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('receita_detail', args=[self.pk])

    def get_absolute_url_update(self):
        return reverse('receita_edit',args=[self.pk])

    def __str__(self):
        return self.nome


