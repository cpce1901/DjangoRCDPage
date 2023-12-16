from django.urls import path
from .views import (
    MobileTokenApiView,
    MobileTokenDetail,
    BudgetList,
    BudgetDetail,
)

app_name = "private_app"

urlpatterns = [
    path("budgets/", BudgetList.as_view(), name="budgets"),
    path("budgets/<int:pk>/", BudgetDetail.as_view(), name="budget-detail"),
    path("mobile-token/", MobileTokenApiView.as_view(), name="mobile-token"),
    path("mobile-token/<int:pk>/", MobileTokenDetail.as_view(), name="mobile-token-detail"),

]
