from django.urls import path
from vistas_generic.views import PublisherLIstview

urlpatterns = [
    path('publishers/', PublisherLIstview.as_view(), name='publisher'),
]
