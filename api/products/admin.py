from django.contrib import admin
from .models import Product
from api_register.models import Register

admin.site.register(Product)
admin.site.register(Register)