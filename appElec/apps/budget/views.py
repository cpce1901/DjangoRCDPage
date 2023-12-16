from django.views.generic import TemplateView
from .models import Budget, MaterialGroup


# Create your views here.
class BudgetList(TemplateView):
    template_name = "private/BadgetList.html"

    def get_context_data(self, **kwargs):
        context = super(BudgetList, self).get_context_data(**kwargs)
        context["budgets"] = Budget.objects.all()
        return context


class BudgetDetail(TemplateView):
    template_name = "private/BadgetDetail.html"

    def get_context_data(self, **kwargs):
        context = super(BudgetDetail, self).get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        context["budget"] = Budget.objects.filter(id=pk).first()
        context["MaterialsGroup"] = MaterialGroup.objects.all()
        return context
