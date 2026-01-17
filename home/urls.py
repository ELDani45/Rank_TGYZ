from django.urls import path
from .views import Login, Home

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('login/', Login.as_view(), name="login")
]
