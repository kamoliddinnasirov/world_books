from django.contrib import admin
from catalog.models import Author, Genre, Language, Publisher, Status, Book, BookInstance



admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
admin.site.register(Book)
admin.site.register(BookInstance)