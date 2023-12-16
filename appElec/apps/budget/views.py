from django.views.generic import TemplateView
from .models import Budgets


# Create your views here.
class BudgetList(TemplateView):
    template_name = "private/BadgetList.html"

    def get_context_data(self, **kwargs):
        context = super(BudgetList, self).get_context_data(**kwargs)
        context["budgets"] = Budgets.objects.all()
        return context


class BudgetDetail(TemplateView):
    template_name = "private/BadgetDetail.html"

    def get_context_data(self, **kwargs):
        context = super(BudgetDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context["budget"] = Budgets.objects.filter(id=pk).first()
        return context
