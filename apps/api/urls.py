import apps
from django.conf.urls import include, url
from django.conf import settings
from importlib import import_module

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

apps_list = apps.__all__
ordered_app_list = [app for app in settings.INSTALLED_APPS if app in apps_list]

# loop on the apps
for app in ordered_app_list:
    # if app.api.urls exists
    urls_module = '{}.api.urls'.format(app)
    try:
        import_module(urls_module)
    except ImportError, e:
        # Ignore "no module named", raise on real errors
        if 'No module named' in str(e) and 'urls' in str(e):
            raise
    else:
        urlpatterns += [
            url(r'^', include(urls_module))
        ]
