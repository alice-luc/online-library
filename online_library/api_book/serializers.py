from rest_framework import serializers
from api_book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


# class BookContentSerializer(serializers.Serializer):
#
