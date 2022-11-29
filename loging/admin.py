from django.contrib import admin
from .models import Producto, Estado_producto, Categoria, Envio
# Register your models here.



class PubliarAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
admin.site.register(Producto, PubliarAdmin)

admin.site.register(Estado_producto)

admin.site.register(Categoria)

admin.site.register(Envio)
