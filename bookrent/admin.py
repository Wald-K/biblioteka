from django.contrib import admin
from . models import Author, Book, Client, Rental

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Client)
admin.site.register(Rental)
