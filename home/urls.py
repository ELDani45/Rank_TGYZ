from django.urls import path
from home.views import Login, Registration, Home
from vistas_generic.views import CreateAuthor


urlpatterns = [
    # esta es la forma mas directa de renderizae un template
    # path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('', Home.as_view(), name='index'),
    path('login/', Login.as_view(), name="login"),
    path('registration/', Registration.as_view(), name="registration"),
    path('autores/', CreateAuthor.as_view(), name='authors')
]
