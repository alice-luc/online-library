import json

from api_book.models import Book
from django.shortcuts import get_object_or_404
from api_book.serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from api_book.services import read_pdf
from api_user.models import UserBookActivity


class BookViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Book.objects.prefetch_related()
    serializer_class = BookSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        file_path = instance.pdf_file
        page_num = get_user_active_page(request.user.id)
        # print(request.user.id)
        book_content = read_pdf(file_path, page_num)
        # print(f'content: {book_content}')
        return Response({**serializer.data, 'content': book_content.get('pages')[0].extract_text()})


def get_user_active_page(user_id: int) -> int:
    # print(UserBookActivity.objects.get(user=user_id).page_number)
    return UserBookActivity.objects.get(user=user_id).page_number
