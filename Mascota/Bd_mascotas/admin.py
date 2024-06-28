from django.contrib import admin

from .models import Mascota, MascotaServicio,Producto,ProductoUsuario,Servicio,Usuario,Post, Categoria, Contacto

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("id_persona","user","pas","tipo","nom","ape","dir","tel","correo","foto")
admin.site.register(Usuario,UsuarioAdmin)

class MascotaAdmi(admin.ModelAdmin):
    list_display=("id_mas","tipo_mas","raza","nom_mas","fecha_nac","foto_mas","id_usuario")
admin.site.register(Mascota,MascotaAdmi)

class MascotaServicioAdmin(admin.ModelAdmin):
    list_display=("codigo","id_servicio","id_mascota","fecha_servicio")
admin.site.register(MascotaServicio,MascotaServicioAdmin)

class ServicioAdmin(admin.ModelAdmin):
    list_display=("id_serv","nom","descripcion","precio","imagen")
admin.site.register(Servicio,ServicioAdmin)

class ProductoUsuarioAdmin(admin.ModelAdmin):
    list_display=("codpu","id_persona","id_pro","cant","total")
admin.site.register(ProductoUsuario,ProductoUsuarioAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display=("id_producto","nom_pro","desc_pro","precio_pro","foto_pro","stock_pro")
admin.site.register(Producto,ProductoAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display=("titulo","contenido","fecha","imagen","Fcreacion","Fedicion")
    ordering=('titulo','fecha')
    list_filter=('id_persona_id__nom','titulo')
admin.site.register(Post,BlogAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display=("nom","FCreacion")
admin.site.register(Categoria,CategoriaAdmin)

class ContactoAdmin(admin.ModelAdmin):
    list_display=("codigo","nombre","email_con","asunto","mensaje")
admin.site.register(Contacto,ContactoAdmin)
