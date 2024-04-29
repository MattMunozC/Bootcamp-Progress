from django.shortcuts import render
from django.http import HttpResponse
from pages.forms import CollaboratorsForm,ClientForm,AdminitratorForm
from django.contrib.auth.decorators import login_required,permission_required
from pages.models import Category,Collaborator,Client,Tier
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth import logout

from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect("/")
# Create your views here.
def home(requests):
    return render(requests,"index.html",context={"DocumentName":"Landing Page"})
def list_clients(request):
    clientes=[]
    return render(request,'client.html',context={"clients":clientes,"DocumentName":"Clientes"
        })
@login_required
@permission_required('pages.add_Collaborator',raise_exception=True)
def register_collab(request):
    if request.method=="POST":
        form=CollaboratorsForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            try:
                cat=Category.objects.get(name=data['categories'])
                Collaborator.objects.create(name=data['name'],
                                            contact=data['contact'],
                                            category=cat).save()
            except Category.DoesNotExist:
                print("Categoria no existe")
    return render(request,"collaborators.html",{"form":CollaboratorsForm(),"DocumentName":"Registrar Colaborador"})
def register_client(request):
    if request.method=="POST":
        form=ClientForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            try:
                user=get_user_model().objects.create(first_name=data['first_name'],
                                      last_name=data["last_name"],
                                      username=data['username'],
                                      password=data['password'])
                user.save()
                Client.objects.create(user=user,
                                      birthday=data['birthday'],
                                      birthplace=data['birthplace'],
                                      tier=Tier.objects.get(name="Bronce")).save()

            except:
                pass
    return render(request,"register_client.html",{"form":ClientForm(),"DocumentName":"Registrar Cliente"})

@login_required
def welcome(request):

    return render(request,"bienvenido.html",{"DocumentName":"Bienvenida","user":f"{request.user.first_name} {request.user.last_name}"})

def register_admin(request):
    if request.method=="POST":
        form=AdminitratorForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            try:
                user=get_user_model().objects.create(first_name=data['first_name'],
                                      last_name=data["last_name"],
                                      username=data['username'],
                                      password=data['password'])
                user.groups.add(Group.objects.get(name="Administrator"))
                user.save()
            except get_user_model().DoesNotExist:
                pass
    return render(request,"register_client.html",{"form":AdminitratorForm(),"DocumentName":"Registrar Administrador"})
def a(requests):
    print(requests.user.groups.all())
    return HttpResponse(requests.user.groups.all()[0].permissions.all())
