from django.db import models
# creación de slugs automaticos
from django.utils.text import slugify
# configuración de pre-save
from django.db.models.signals import pre_save
# evitar slugs duplicados
import uuid


# Create your models here.
class Product(models.Model):
    """
    Model representing a product
    """
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ImageField(
        upload_to='products/',
        null=False, blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    # los slugs se usaran para identificar los productos
    # de forma indiviual
    slug = models.SlugField(
        max_length=200,
        null=False,
        blank=False,
        unique=True,
        )

    # para que se muestre el nombre del producto en el admin
    def __str__(self):
        return self.title


# se encarga de que se guarde el slug antes de crear el neuvo producto
def new_slug(sender, instance, *args, **kwargs):

    if instance.title and not instance.slug:
        # si no se tiene un titulo, ni se tiene slug
        slug = slugify(instance.title)

        # verificamos que el slug exista, si existe, generamos un nuevo slug
        while Product.objects.filter(slug=slug).exists():
            # crearemos un slug únio, usando el titulo del producto
            # luego usaremos la libreria para generar un número aletario
            # de 8 caracteres, para eso se usa el slice [:8] que limita a 8
            slug = slugify(
               '{}-{}'.format(instance.title, str(uuid.uuid4())[:8])
            )
        # guardamos el slug luego de crearlo
        instance.slug = slug


# se conecta el pre_save con la funcion new_slug
# para que se ejecute antes de guardar el producto
pre_save.connect(new_slug, sender=Product)
