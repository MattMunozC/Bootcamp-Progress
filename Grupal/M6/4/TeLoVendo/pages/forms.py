from django import forms
from pages.models import Category

class CollaboratorsForm(forms.Form):
    name=forms.CharField(max_length=100,label="Nombre del colaborador",required=True)
    contact=forms.IntegerField(label="Numero de contacto",required=True,widget=forms.NumberInput(attrs={'min':10000000}))
    category=[
        ('electrodomesticos','Electrodomesticos'),
        ('celulares','Celulares'),
        ('computadores','Computadores'),
        ('componentes','Componentes')
    ]
    categories=forms.ChoiceField(choices=category,widget=forms.Select())