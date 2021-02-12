from django import forms
from. models import Todos
class Listform(forms.ModelForm):
    class Meta:
        model= Todos
        fields=["title","description","finished","date"]