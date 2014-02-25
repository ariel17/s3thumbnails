from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 's3thumbnails.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^images/', include('images.urls')),
)


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        r'static/',
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        r'media/',
        document_root=settings.MEDIA_ROOT
    )
