from rest_framework import serializers
from api_book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


<<<<<<< HEAD:online_library/api_book/serializers.py
# class BookContentSerializer(serializers.Serializer):
#
=======
class BookContentSerializer(serializers.Serializer):
    
>>>>>>> bb3e198f1e4519d486ace0fe854793f2cdc5f1c4:online_library/api/serializers.py
