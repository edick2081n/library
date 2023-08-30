from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    book_author = models.ManyToManyField(Author)

    def __str__(self):
        return self.name
