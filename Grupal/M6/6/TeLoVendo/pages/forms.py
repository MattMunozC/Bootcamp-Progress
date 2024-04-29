from django import forms
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


    
class ClientForm(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    birthdate=forms.DateField(required=True)
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())
    birthplace=forms.CharField(max_length=100)

class AdminitratorForm(forms.Form):
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())