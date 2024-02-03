from django.contrib import admin
from . models import Book, Publisher

# Register your models here.
admin.site.register(Book)
admin.site.register(Publisher)