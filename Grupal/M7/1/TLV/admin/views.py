from django.shortcuts import render
from django.http import HttpResponse
from account.decorators.permissionsDecorator import staff_required,superuser_required
from .forms import ProductModelForm
# Create your views here.
@staff_required
def admin_page(request):
    pass
@staff_required
def add_product(request):
    return render(request,"admin_add_product.html",{
        "form": ProductModelForm()
    })

@staff_required
def sell_product(request):
    pass
