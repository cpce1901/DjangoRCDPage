from rest_framework.routers import DefaultRouter
from .viewsets import TagsViewSet, ProviderViewSet, MaterialViewSet

router = DefaultRouter()

router.register(r"tags", TagsViewSet)
router.register(r"providers", ProviderViewSet)
router.register(r"materials", MaterialViewSet)

urlpatterns = router.urls