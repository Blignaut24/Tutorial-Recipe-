from django.views.generic import TemplateView


class Index(TemplateView):
    """
    This class-based view loads the 'home/index.html' template.
    """
    template_name = 'home/index.html'