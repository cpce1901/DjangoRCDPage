from rest_framework.routers import DefaultRouter
from .viewsets import MessageViewSet, MobileTokenViewSet

router = DefaultRouter()

router.register(r"messages", MessageViewSet)
router.register(r"mobile-token", MobileTokenViewSet)

urlpatterns = router.urls