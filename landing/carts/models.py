from django.db import models
from users.models import User
from products.models import Product
from django.db.models.signals import pre_saves


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
