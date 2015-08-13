from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    # List of apps sitemaps goes here
}

admin.autodiscover()

urlpatterns = staticfiles_urlpatterns()


urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^robots.txt$', include('robots.urls')),
)

urlpatterns += patterns('utils.views',
    url(r'^$', 'load_template', {'template_name': 'index.html'}, name='home'),

)

if settings.DEVELOPMENT:
    urlpatterns += patterns('',
        # TODO/WARNING: media url is hard coded in auto complete templates
        url(r'^media/(?P<path>.*)$','django.views.static.serve',
            {'document_root':  getattr(settings, 'MEDIA_ROOT', '/media')}),
    )
