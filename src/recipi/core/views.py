from django.views.generic import TemplateView


class IndexView(TemplateView):
    """View for the index page"""
    template_name = 'recipi/core/index.html'
