from django.urls import path
from .views import (
    BudgetList,
    BudgetDetail,
)

app_name = "budget_app"

urlpatterns = [
    path("budgets/", BudgetList.as_view(), name="budgets"),
    path("budgets/<int:pk>/", BudgetDetail.as_view(), name="budget-detail"),

]