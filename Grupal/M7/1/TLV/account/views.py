from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils.timezone import now
from .forms import userForm
from .models import User,Client
# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('/')
def signup(request):
    if request.method=="POST":
        form=userForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            try:
                user=User.objects.get(username=data["username"])
                client=Client.objects.get(user=user)
            except User.DoesNotExist or Client.DoesNotExist:
                user=User.objects.create(first_name=data["first_name"],
                                            last_name=data["last_name"],
                                            username=data['username'],
                                            password=data["password"],
                                            email=data["email"],
                                            date_joined=now(),
                                            is_active=True,
                                            is_superuser=False,
                                            is_staff=False
                                        )
                client=Client.objects.create(user=user)
                user.save()
                client.save()
                return redirect("/account/login")
    return render(request,"registration/signup.html",context=
                  {
                      "DocumentName":"Registrarse",
                      "form":userForm(),
                      "styles":[
                          "account_login",
                          "account_signup"
                      ]
                  })