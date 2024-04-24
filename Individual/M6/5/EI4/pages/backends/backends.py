from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from pages.models import usuario

class UsuarioAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = usuario
        print(username,password)
        user=User.objects.filter(nombre_usuario=username).first()
        try:
            if user.check_password(password):
                return user
        except:
            return None
        