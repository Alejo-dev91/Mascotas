from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Post, Servicio, Producto, Contacto
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import BlogForms
from .forms import ContactoForm
from django.contrib import messages



"""def blog(request):
    post=Post.objects.all()
    return render(request, "Bd_mascotas/blog.html",{'blog':post})
"""



#CBV en la CRUD : LISTVIEW - POST Y CATEGORIA DEL TEMPLATE BLOG

class BlogListView(ListView):
    model=Post
    paginate_by=1
    

    #Obtener los objetos de la tabla post
    def get_queryset(self):
        return Post.objects.all()
    
    #envia informacion adicional la cual sirve para poder paginar
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        return context
    
#CBV en la CRUD: CREATEVIEW -POST Y CATEGORIA DEL TMEPLATE BLOG

class BlogCreate(CreateView):
    model=Post #tabla
    form_class=BlogForms # formulario creado en el forms.py
    template_name='Bd_mascotas/CreateBlog.html'# pagina html donde esta el formulario
    success_url=reverse_lazy('listarPosters') 
      
def portafolio(request):
    producto=Producto.objects.all()
    return render(request,"Bd_mascotas/portfolio.html",{'productos':producto})


def servicios(request):
    servicio=Servicio.objects.all()
    return render(request,"Bd_mascotas/services.html",{'servicios':servicio})

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            contacto = formulario.save(commit=False)
            # Asigna un valor incremental al campo código
            try:
                ultimo_contacto = Contacto.objects.order_by('-codigo').first()
            except Contacto.DoesNotExist:
                ultimo_contacto = None

            nuevo_codigo = ultimo_contacto.codigo + 1 if ultimo_contacto else 1
            contacto.codigo = nuevo_codigo
            contacto.save()
            messages.success(request,"Formulario enviado exitosamente")
            return redirect(to="contact")
    else:
        formulario = ContactoForm()
    return render(request, "Bd_mascotas/contact.html", {'form': formulario})






