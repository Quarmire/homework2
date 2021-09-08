from django.contrib import admin
from .models import MyFirstModel, Age

# Register your models here.

admin.site.register(MyFirstModel)
admin.site.register(Age)