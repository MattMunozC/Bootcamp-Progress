from django.urls import path
from .views import add_product,admin_page,sell_product
urlpatterns=[
    path("",admin_page),
    path("agregar_producto",add_product),
    path("vender_producto",sell_product)
]