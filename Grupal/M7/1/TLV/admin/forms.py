from retail.models import Product
from django import forms
class ProductModelForm(forms.ModelForm):
    class Meta():
        model=Product
        fields='__all__'