from rest_framework import routers

from api.views import BookViewSet

router = routers.SimpleRouter()
router.register(r'books', BookViewSet)
