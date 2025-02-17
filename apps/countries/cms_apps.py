from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class CountriesApphook(CMSApp):
    app_name = "countries"
    name = "Countries Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["apps.countries.urls"]