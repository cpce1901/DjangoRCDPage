from rest_framework.routers import DefaultRouter
from .viewsets.tags_viewset import TagsViewSet
from .viewsets.provider_viewset import ProviderViewSet

router = DefaultRouter()

router.register(r"tags", TagsViewSet)
router.register(r"providers", ProviderViewSet)

urlpatterns = router.urls
