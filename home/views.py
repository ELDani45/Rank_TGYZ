# from django.shortcuts import render
from django.views.generic import TemplateView
# Importamos la herramineta { VIEW } para indicarle a django que vamos a hacer una calse que sera una vista.

# Create your views here.


class Home(TemplateView):
    template_name = "index.html"
