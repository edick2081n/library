from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    book_author = serializers.SlugRelatedField(many=True, read_only=False, queryset=Author.objects.all(),
                                               slug_field='name')
    class Meta:
        model = Book
        fields = ['id', 'name', 'book_author']


