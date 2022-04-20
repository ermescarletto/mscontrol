from django import forms



class ChecklistForm(forms.Form):
    inicio_checklist = forms.DateTimeField()
    ambiente = forms.IntegerField()
    servico = forms.IntegerField()
    checklist = forms.IntegerField()
    item = forms.IntegerField()
    valor_item = forms.BooleanField()
    imagem = forms.ImageField()
    fim_checklist = forms.DateTimeField()

