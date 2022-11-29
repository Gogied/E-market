from django import forms
from .models import Producto


class PublicarForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo','descripcion','estado_id','precio','contacto','categoria_id','envio_id']
        widget = {
            'descripcion': forms.TextInput(attrs={'class':'form-control'})
        }

