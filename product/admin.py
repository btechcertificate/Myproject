from django.contrib import admin

from product.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ("id", "name", "is_active")

admin.site.register(Product, ProductAdmin)
