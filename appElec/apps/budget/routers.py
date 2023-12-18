from rest_framework.routers import DefaultRouter
from .viewsets import ClientsViewSet, ItemsViewSet, BudgetsViewSet


router = DefaultRouter()

router.register(r"clients", ClientsViewSet)
router.register(r"items", ItemsViewSet)
router.register(r"budgets", BudgetsViewSet)

urlpatterns = router.urls