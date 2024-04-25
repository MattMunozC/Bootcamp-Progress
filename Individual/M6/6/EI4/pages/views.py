from django.shortcuts import render
from pages.models import usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect
from pages.forms import RegisterForm
from pages.models import usuario
from datetime import datetime
from django.contrib.auth.models import Group
from django.utils import timezone
from pages.decorators.restrictionDecorator import post_only,adult_only,child_only

# Create your views here.
def home(requets):
    if requets.method=="POST":
        form=RegisterForm(requets.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=usuario.objects.create(first_name=data["first_name"],
                                        last_name=data["last_name"],
                                        username=data['username'],
                                        password=data["password"],
                                        email=data["email"],
                                        date_joined=timezone.make_aware(datetime.now(), timezone.get_current_timezone()),
                                        is_active=True,
                                        is_superuser=False,
                                        age=data["age"]
                                        )
            if user.age<18:
                print("the user is a child")
                child=Group.objects.get(name='Child')
                user.groups.add(child)
            else:
                print("the user is an adult")
                user.groups.add(Group.objects.get(name="adult"))
            try:
                user.save()
            except:
                pass
    return render(requets,"index.html",{"form":RegisterForm()})

@login_required
def status_view(request):
    return render(request,"status.html",context={"user":request.user,"child":request.user.age<18})

@login_required
def lista_usuarios(request):
    username=request.user.username
    print(usuario.objects.get(username=username).groups.all())
    return HttpResponse(f"<h1>hola {username}</h1>",content_type="text/html")
@login_required
def otra_vista(request):
    print(request.user.groups)
    return HttpResponse("<h1>hola mundo</h1>")

@login_required
@adult_only
def restricted_view(request):
    return HttpResponse("Tu eres un adulto")

@login_required
@child_only
def frootloops(request):
    return HttpResponse("<img src='https://i5.walmartimages.com/seo/Kellogg-s-Froot-Loops-Original-Breakfast-Cereal-Mega-Size-28-oz-Box_f042ed22-618b-4020-9ea5-bd153962de2e.5bf12167b8a22165ce399c60d38bf877.jpeg' style='height:100vh'>")

def logout_view(request):
    logout(request)
    return redirect("/")