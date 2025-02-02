# from django.conf.urls import include, url
# from django.contrib import admin

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'vid.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),

#     url(r'^admin/', include(admin.site.urls)),
# ]

from django.contrib import admin

from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailsearch.urls import frontend as wagtailsearch_frontend_urls

from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^django-admin/', include(admin.site.urls)),

  url(r'^admin/', include(wagtailadmin_urls)),
  url(r'^search/', include(wagtailsearch_frontend_urls)),
  url(r'^documents/', include(wagtaildocs_urls)),

  # Optional urlconf for including your own vanilla Django urls/views

  # For anything not caught by a more specific rule above, hand over to
  # Wagtail's serving mechanism
  url(r'', include(wagtail_urls)),
)
