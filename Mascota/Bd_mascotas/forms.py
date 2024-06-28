from django import forms
from .models import Post, Contacto

class BlogForms(forms.ModelForm):
    
    class Meta:
        model=Post
        
        fields='__all__'
        #fields=['imagen'] este es para llamar de uno en uno

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model=Contacto
        fields=['nombre', 'email_con','asunto', 'mensaje']
        
      # Este es el formulario que se muestra en el contact.html con {{form}}  
    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escribe tu nombre'
        })
        self.fields['email_con'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escribe tu email'
        })
        self.fields['asunto'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escribe el asunto'
        })
        self.fields['mensaje'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escribe tu mensaje'
        })