from django.shortcuts import render
from rest_framework import viewsets
from selection.models import Author, Book
from selection.serializers import AuthorSerializer, BookSerializer
import selection


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def list_book(request):
    authors_list = Author.objects.all()
    return render(request, 'selection/authors.html', {'authors_list':authors_list})
