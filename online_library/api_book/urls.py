from django.urls import path

from api_book.views import BookViewSet

urlpatterns = [
    path('book/<int:pk>/', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'})),
]
