
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views as core_views
from Bd_mascotas import views as bd
from Bd_mascotas.views import BlogListView, BlogCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_views.main),
    path('contact/',bd.contacto,name='contact'),
    path('services/',bd.servicios),
    #path('blog/',bd.blog),
    path('portfolio/',bd.portafolio),
    path('ingresar/',core_views.login),
    path('registro_u/',core_views.registroU),
    
    #CRUD PARA LA TABLA POST
    path('blog/',BlogListView.as_view(), name='listarPosters'),
    path('Crear/',BlogCreate.as_view(),name='CreatePoster'),
    
]

# codigo para verificar las imagenes cargadas

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
