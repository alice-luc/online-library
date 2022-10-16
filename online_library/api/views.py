from api.models import Book
from django.shortcuts import get_object_or_404
from api.serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class BookViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Book.objects.prefetch_related()
    serializer_class = BookSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
