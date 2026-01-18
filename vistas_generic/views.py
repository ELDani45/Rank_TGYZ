# from django.shortcuts import render
from django.views.generic import ListView
from vistas_generic.models import Publisher


class PublisherLIstview(ListView):
    model = Publisher
    template_name = 'vistas/publisher_list.html'
