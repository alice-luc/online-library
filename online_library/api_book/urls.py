from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

# from api_book.routers import router
from api_book.views import BookViewSet

urlpatterns = [
    path('book/<int:pk>/', BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('books/', BookViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
