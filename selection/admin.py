from django.contrib import admin
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'authors_name']

    def authors_name(self, book):
        authors = []
        for author in book.book_author.all():
            authors.append(author.name)
        return ", ".join(authors)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_count']

    def book_count(self, author):
        books = []
        for book in author.book_set.all():
            books.append(book.id)
        return str(len(books))


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
