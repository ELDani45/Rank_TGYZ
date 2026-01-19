from vistas_generic.models import Author
from django import forms


class MakeAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['salutation', 'name', 'email', 'headshot']
