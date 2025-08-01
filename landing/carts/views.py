from django.shortcuts import render
from .models import Cart
from .functions import createCart

# Create your views here.
def cart(request):
    # request.session.set_expiry(300)  # set 5 minutos de sessión
    # key = request.session.session_key
    # print(f'Session Key: {key}')
    cart = createCart(request)

    return render(request, 'carts/carts.html', {})

def add(request):
    """
    Función para agregar productos al carrito
    """
    cart = createCart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))
    
    cart.products.add(product)
