# from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from vistas_generic.models import Publisher, Author
from vistas_generic.models import Book
from django.urls import reverse_lazy
from vistas_generic.forms import MakeAuthor


class PublisherLIstview(ListView):
    model = Publisher
    template_name = 'vistas/publisher_list.html'
    context_object_name = "my_favorite_publishers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_list"] = Book.objects.all()
        return context

# c Cuando queremos crear un objeto, lo hacemos con la clase ' CreateView ' que viene por defecto en django


class CreateAuthor(CreateView):
    model = Author

    # reverse_lazy se utiliza para que django sepa a donde tiene que redirigir despues de creado el objeto o instancia
    success_url = reverse_lazy('autores')

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            return render(request, "authors.html", {
                'form': MakeAuthor
            })

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            try:  # Aqui intentamos crear un ususario
                # Aqui le enviamos los datos con ' request '
                form = MakeAuthor(request.POST, request.FILES)
                if form.is_valid():  # aqui validamos si los datos son validos
                    form.save()  # Guardamos si los son
                    # retornamos despuesaa otra vista
                    return render(request, 'index.html')
                else:
                    # si no es correcto los datos, devolvemos al usuario a la vista principal y mostramos el error
                    return render(request, "authors.html", {
                        'form': form
                    })
            except ValueError:
                return render(request, "authors.html", {
                    'form': MakeAuthor
                })
