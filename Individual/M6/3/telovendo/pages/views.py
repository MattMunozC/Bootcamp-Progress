from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def landing_page(request):
    return render(request,"index.html")

def see_users(requests,page_name):
    users=User.objects.all()
    return render(requests,f"user_view/{page_name}",context={"user_list":users})