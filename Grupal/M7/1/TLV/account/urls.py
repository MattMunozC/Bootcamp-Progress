from django.urls import path
from django.contrib.auth.views import LoginView
from .views import logout_view,signup
urlpatterns=[
   path('login',LoginView.as_view(),name="login"),
    path("logout",logout_view,name="logout"),
    path("signup",signup),
]
