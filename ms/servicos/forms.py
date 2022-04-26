from django import forms
from .models import *


class ChecklistForm(forms.Form):
    ambiente = forms.IntegerField()
    checklist = forms.IntegerField()
    itens = forms.JSONField()
    imagem = forms.ImageField()

    class Meta:
        model = ChecklistPreenchido