from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Product
# importamos Q para aplicar filtros
from django.db.models import Q


# Create your views here.
class ProductListView(ListView):
    """
    List view for displaying products.
    Esta función obtiene los productos actuales
    y le pasa a la template index la lista de productos.
    """
    template_name = 'index.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pasamos a nuestro contexto la lista de productos
        # esta se encuentra en el query set
        context['products'] = 'Products'
        return context


class ProductDetailView(DetailView):
    """
    Detail view for displaying product details.
    Obtiene el producto por su id (pk) y lo muestra
    en la template products.html
    """
    model = Product
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class ProductSearchListView(ListView):
    """
    Esta vista permite la busqueda dinamica de productos
    """
    template_name = 'products/search.html'

    def get_queryset(self):
        """
        Filtra los productos hasta hallar el solicitado
        Sin importar que este en mayusculas o minusculas
        """
        # usamos Q para aplicar filtros
        # Busca ya sea por titulo o categoria
        filters = Q(title__icontains=self.query()) | Q(category__title__icontains = self.query())

        return Product.objects.filter(filters)

    def query(self):
        """
        Se obtiene el parametro de la busqueda del producto
        en este caso se llamo 'product',
        está en el templates/product/search.html
        """
        return self.request.GET.get('product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()

        return context
