from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'clothing.views.home', name='home'),
    url(r'^department/(?P<department_slug>[\w\-]+)/$', 'clothing.views.department', name='department'),
    url(r'^department/(?P<department_slug>[\w\-]+)/category/(?P<category_name_slug>[\w\-]+)/$', 'clothing.views.category', name='category'),
    url(r'^department/(?P<department_slug>[\w\-]+)/(?P<product_slug>[\w\-]+)/$', 'clothing.views.product', name='product'),
    url(r'^stores/', 'clothing.views.stores', name='stores'),
    url(r'^store/(?P<store>[\w\-]+)/$', 'clothing.views.store', name='store'),
    url(r'^cart/', 'clothing.views.cart', name='cart'),
    url(r'^search/$', 'clothing.views.search', name='search'),
    url(r'^about/', 'clothing.views.about', name='about'),
    url(r'^testing/', 'clothing.views.testing', name='testing'),
    # url(r'^cart/add/', 'clothing.views.addToCart', name='addToCart'),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), )