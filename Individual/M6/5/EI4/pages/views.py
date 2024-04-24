from django.shortcuts import render
from pages.models import usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect

def post_only(func):
    def wrapper(request):
        if request.method=='POST':
            return func(request)
    return wrapper
# Create your views here.
def home(requets):
    return render(requets,"index.html")
@post_only
def nuevo_usuario(request):
    post_data=request.POST
    data=list(post_data.values())[1::]
    nuevo=usuario(*([1]+data))
    nuevo.save()
    return render(request,"index.html")
@login_required
def lista_usuarios(request):
    username=request.user.nombre_usuario
    return HttpResponse(f"<h1>hola {username}</h1>",content_type="text/html")
@login_required
def otra_vista(request):
    return HttpResponse("<h1>hola mundo</h1>")

def logout_view(request):
    logout(request)
    return redirect("/")