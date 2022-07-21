from django import forms
from custom.models import Cliente


class formaCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'