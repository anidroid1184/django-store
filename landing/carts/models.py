from django.db import models
from users.models import User
from products.models import Product
from django.db.models.signals import pre_save
import uuid


# Create your models here.
class Cart(models.Model):
    """
    Model that represents a shoping cart
    """
    # El usuario se representa como una foreing key
    # buul quiere decir que puede ser nulo
    # blank quiere decir que no es obligatorio
    # osea que podemos tener visitantes y usuarios que tengan
    # carritos
    cart_id = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        unique=True
        )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.CASCADE
        )
    products = models.ManyToManyField(Product)
    subtotal = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # retornamos el id del carrito
        return self.cart_id
    

def set_cart_id(sender, instance, *args, **kwargs):
    """
    Función que agrega un valor unico a un visitante anonimo
    para preservar su carrito
    param sender: Modelo que envia la señal(Cart)
    param instance: Instancia del modelo que envio la señal
    param args: Argumentos adicionales
    param kwargs: Argumentos adicionales
    """
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())


# Conectamos la señal pre_save al modelo Cart
# para que se ejecute la función set_cart_id antes de guardar
pre_save.connect(set_cart_id, sender=Cart)
