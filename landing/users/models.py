from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customers(User):

    """
    Creamos un proxy, una forma de extender
    el modelo existente sin crear una nueva tabla de datos
    """
    class Meta:
        # habilitamos le proxy
        proxy = True

    def get_products(self):
        return []


class Profile(models.Model):
    """
    Model para el perfil del usuario
    """
    # si se elemina el usuario, se elimina
    # el profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografy = models.TextField()
