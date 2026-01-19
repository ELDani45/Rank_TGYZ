from vistas_generic.models import Author
from django import forms

# Para hace de un modelo un formulario:
# 1 - primero debemos de importat el modelo que vamos a utilizar
# 2 -luego de " forms " llamamos al comando de " ModelfForm "
# 3 -Dentro de la clase creamos otra clase con eo nombre especial de " Meta "
# 4 - Ahi dentro definimos la siguientes variiables: [ " model " y " fields " ]


class MakeAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['salutation', 'name', 'email', 'headshot']
