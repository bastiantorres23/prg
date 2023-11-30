from django import forms
from .models import Zapato

class articleform(forms.ModelForm):
    class Meta:
        model = Zapato
        fields= ['Id','Nombrez','imgend','precioz','catego','gene']
        labels= {
            'Id': 'ID del Producto',
            'Nombrez': 'Nombre',
            'imgend': 'Img',
            'precioz': 'Precio',
            'catego': 'Categoria',
            'gene': 'Genero',
        }
        widgets = {
            'Id': forms.NumberInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el ID',
                    'id':'Id'
                }
            ),
            'Nombrez': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre',
                    'id':'Nombrez'
                }
            ),

            'precioz': forms.NumberInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese el Precio',
                    'id':'precioz'
                }
            ),

        }
