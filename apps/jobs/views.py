from django.views.generic import TemplateView
from generic.utils import get_css_and_js_link_from_vite_assets


class JobsView(TemplateView):
    template_name = "jobs/job_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve CSS and JS links from Vite asset manifest
        # Remove the main_js_links
        css_links, js_links, main_js_links = get_css_and_js_link_from_vite_assets("jobs")
        context["css_links"] = css_links
        context["js_links"] = js_links
        return context
