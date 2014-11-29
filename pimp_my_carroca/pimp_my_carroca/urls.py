import settings

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pimp_my_carroca.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^maps/', include('maps.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT})
    )
