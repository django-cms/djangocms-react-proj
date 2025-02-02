from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class GistApphook(CMSApp):
    app_name = "gist"
    name = "Gist Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["apps.gist.urls"]