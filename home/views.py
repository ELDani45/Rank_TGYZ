# from django.shortcuts import render
from django.views.generic import TemplateView  # Lista basada en clase
from home.forms import SignIn, Registrate
# Importamos la herramineta { VIEW } para indicarle a django que vamos a hacer una calse que sera una vista.

# Create your views here.


class Home(TemplateView):  # se coloca " TemplateView " para que django interprete que esta clase es una vista
    template_name = "index.html"


class Login(TemplateView):
    template_name = "login.html"

    # metodo interno que trae toda vista de clase basda en Django para definir el contexto que se va a enviar al template
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["signin"] = SignIn()
        return contex


class Registration(TemplateView):
    template_name = "registration.html"

    # metodo interno que trae toda vista de clase basda en Django para definir el contexto que se va a enviar al template
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex["registration"] = Registrate()
        return contex
