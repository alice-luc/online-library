import json

from api.models import Book
from django.shortcuts import get_object_or_404
from api.serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from api.services import read_pdf


class BookViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Book.objects.prefetch_related()
    serializer_class = BookSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     file_path = instance.pdf_file
    #     page_num = 0
    #     book_content = self.read_book(file_path, page_num)
    #     # print(f'content: {book_content}')
    #     # return JSON.
    #     return Response({**serializer.data, 'content': book_content.get('pages')})
    #         # "book_content": book_content

        # })
        # return Response(serializer.data)


class BookContentViewSet(viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    @staticmethod
    def read_book(path: str, page_num: int) -> object:
        return read_pdf(path, page_num)
    # permission_classes = [IsAccountAdminOrReadOnly]
