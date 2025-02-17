from django.shortcuts import render

from django.views.generic import TemplateView
from generic.utils import get_css_and_js_link_from_vite_assets


class CountriesView(TemplateView):
    template_name = "countries/country-list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        css_links, js_links, main_js_links = get_css_and_js_link_from_vite_assets("countries", uses_client=True)
        context["css_links"] = css_links
        context["js_links"] = js_links
        return context
