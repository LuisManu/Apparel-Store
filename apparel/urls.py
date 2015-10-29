from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User


# from clothing.views import MyRegistrationView


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('clothing.urls')),
    url(r'^basket/', include('cart.urls')),
    url(r'^accounts/', include('auth_app.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), )