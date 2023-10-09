from django.shortcuts import render
from django.views.generic import TemplateView

from menu.models import FoodMenu


class IndexPageView(TemplateView):
    template_name = "foodmenu/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['menu'] = FoodMenu.objects.get(identifier='main_menu')
        except FoodMenu.DoesNotExist:
            context['menu'] = None
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
