from django.shortcuts import render
from pages.models import usuario

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