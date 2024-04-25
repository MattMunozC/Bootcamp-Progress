from django.http import HttpResponse
from django.contrib.auth.models import Group
def post_only(func):
    def wrapper(request):
        if request.method=='POST':
            return func(request)
    return wrapper
def adult_only(func):
    def wrapper(request):
        try:
            group=request.user.groups.get(name='Adult')
            return func(request)
        except Group.DoesNotExist:
            return HttpResponse("<h1>No estas permitico aqui</h1>",status=403)
    return wrapper
def child_only(func):
    def wrapper(request):
        try:
            group=request.user.groups.get(name='Child')
            return func(request)
        except Group.DoesNotExist:
            return HttpResponse("<h1>No estas permitico aqui</h1>",status=403)
    return wrapper