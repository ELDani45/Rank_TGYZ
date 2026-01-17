# from django.shortcuts import render
from django.views.generic import TemplateView
from home.forms import SignIn
# Importamos la herramineta { VIEW } para indicarle a django que vamos a hacer una calse que sera una vista.

# Create your views here.


class Home(TemplateView):
    template_name = "index.html"


class Login(TemplateView):
    template_name = "login.html"

    def Signin(self, request):
        form = SignIn()
        if request.method == "GET":
            return {"form": form}
