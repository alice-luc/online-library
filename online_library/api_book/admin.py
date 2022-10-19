from django.contrib import admin
<<<<<<< HEAD:online_library/api_book/admin.py
from api_book.models import Book, Author, Genre
=======
from api.models import Book, Author, Genre
>>>>>>> bb3e198f1e4519d486ace0fe854793f2cdc5f1c4:online_library/api/admin.py
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
