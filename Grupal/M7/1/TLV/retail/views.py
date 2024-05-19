from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"retail_home.html",context={
        "DocumentName":"Te lo vendo",
        "user": request.user.username if request.user.username!="AnonymousUser" else False
    })