from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Status)
admin.site.register(PayingMethod)
admin.site.register(Shopping)
admin.site.register(Checkout)
admin.site.register(CheckoutDetail)
