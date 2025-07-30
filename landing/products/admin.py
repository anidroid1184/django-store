from django.contrib import admin
from .models import Product  # importamos el modelo product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    """
    En este modelo se registran los productos
    en el admin de Django.
    También define la tabla que se mostrará en el admin

    En este caso se mostrará el título, la descripción,
    el precio y la fecha de creación del producto.
    Donde list_display son las columnas que se mostrarán
    en la tabla del admin.
    """
    # configuraremos los campos a mostrar en el admin
    fields = ('title', 'description', 'price', 'image')
    # configuramos los campo
    list_display = ('__str__', 'slug', 'created_at')


#  Damos acceso a registrar productos desde el admin
admin.site.register(Product, ProductAdmin)
