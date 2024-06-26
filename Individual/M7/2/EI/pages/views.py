from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from pages.helpers.existHelper import check_user,check_tasks
# Create your views here.
def welcome(request):
    return render(request,"pages_home.html",context={
        "DocumentName":"Bienvenido",
        "styles":["pages_home"]}
        )
@login_required
def home(request): 
    return render(request,"pages_mainpage.html",context={
        "DocumentName":"Inicio",
        "user":check_user(request.user),
        "Task":check_tasks(request.user),
        "styles":["pages_mainpage"]
    })

