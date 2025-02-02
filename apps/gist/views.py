from django.views.generic import TemplateView
from apps.generic.utils import get_css_and_js_link_from_vite_assets


class GistView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        css_links, js_links, main_js_links = get_css_and_js_link_from_vite_assets("gist")
        context["css_links"] = css_links
        context["js_lnks"] = js_links
        return context
