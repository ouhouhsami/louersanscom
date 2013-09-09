#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from sanscom.profiles.urls import profiles_urlpatterns
from ads.models import HomeForRentAd, HomeForRentAdSearch
from ads.filtersets import HomeForRentAdFilterSet

HomeForRentAdFilterSet()

admin.autodiscover()

from moderation.helpers import auto_discover
auto_discover()


home_for_rent_info_dict = {
    'queryset': HomeForRentAd.objects.filter(visible=True),
    'date_field': 'create_date',
}

sitemaps = {
    'flatpages': FlatPageSitemap,
    'homeforrentads': GenericSitemap(home_for_rent_info_dict, priority=0.6),
}

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('search'))),
    url(r'^annonce/', include('louersanscom.ads.urls')),
)

urlpatterns += profiles_urlpatterns(HomeForRentAd, HomeForRentAdSearch)

urlpatterns += patterns('',
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^admin/mails/', include('mail_factory.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^django-rq', include('django_rq.urls'))
)

if settings.DEBUG:
    urlpatterns += patterns('',
                        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT,  'show_indexes': True}))
