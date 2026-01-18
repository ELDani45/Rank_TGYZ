from django.urls import path
from .views import Login, Home, Registration

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('login/', Login.as_view(), name="login"),
    path('registration/', Registration.as_view(), name="registration")
]
