from django.db import models
from products.models import Product


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    # importarmos la relacion muchos a muchos
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
