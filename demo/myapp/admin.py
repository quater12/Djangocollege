from django.contrib import admin

# Register your models here.
from .models import Category, Toy

admin.site.register(Category)
admin.site.register(Toy)