from .models import Cart


def createCart(request):
    """
    Despliega la vista del carrito
    verifica el usuario, en caso de no estar autenticado,
    retorna None
    :param request: HttpRequest
    :return: Renderiza la plantilla del carrito
    """
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    cart = Cart.objects.filter(id=cart_id).first()

    # si no hay carrito previo, se creara uno
    if cart is None:
        cart = Cart.objects.create(user=user)

    # si el usuario se logea, se mantiene el carrito
    if user and cart.user is None:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id

    return cart
