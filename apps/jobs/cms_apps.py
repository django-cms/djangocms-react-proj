from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

@apphook_pool.register
class JobsApp(CMSApp):
    app_name = "jobs"
    name = "Jobs App"

    def get_urls(self, *args, **kwargs):
        return ["apps.jobs.urls"]