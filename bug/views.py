from django.views.generic import TemplateView

from bug.forms import MyForm

# Create your views here.
class FormView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = MyForm()
        return context
