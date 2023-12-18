from django.urls import path
from .views import (
    BudgetsApiView,
    BudgetsDetail,
    ItemsApiView,
    ItemsDetail
)

app_name = "budget_app"

urlpatterns = [
    path("budgets/", BudgetsApiView.as_view(), name="budgets"),
    path("budgets/<int:pk>/", BudgetsDetail.as_view(), name="budget-detail"),
    path("items/", ItemsApiView.as_view(), name="items"),
    path("items/<int:pk>/", ItemsDetail.as_view(), name="items-detail"),

]