from typing import Any
from django import forms
class RegisterForm(forms.Form):
    first_name=forms.CharField(label="Nombre",max_length=100,required=True)
    last_name=forms.CharField(label="Apellido",max_length=100,required=True)
    username=forms.CharField(label="nombre Usuario",required=True)
    password=forms.CharField(label="contraseña",widget=forms.PasswordInput,required=True)
    confirm_password=forms.CharField(label="confime contraseña",widget=forms.PasswordInput,required=True)
    age=forms.IntegerField(label="Edad")
    email=forms.EmailField(label="email")
    def clean(self) -> dict[str, Any]:
        cleaned_data= super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data
    