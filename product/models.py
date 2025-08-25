from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False)
