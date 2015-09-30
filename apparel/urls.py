from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User


from clothing.views import MyRegistrationView

from django.contrib.auth.views import login
from django.contrib.auth.decorators import user_passes_test


login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/')




urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('clothing.urls')),
    # url(r'^$', 'clothing.views.home', name='home'),
    # url(r'^department/(?P<department_slug>[\w\-]+)/$', 'clothing.views.department', name='department'),
    # url(r'^department/(?P<department_slug>[\w\-]+)/category/(?P<category_name_slug>[\w\-]+)/$', 'clothing.views.category', name='category'),
    # url(r'^department/(?P<department_slug>[\w\-]+)/(?P<product_slug>[\w\-]+)/$', 'clothing.views.product', name='product'),
    # url(r'^stores/', 'clothing.views.stores', name='stores'),
    # url(r'^store/(?P<store>[\w\-]+)/$', 'clothing.views.store', name='store'),
    # url(r'^cart/', 'clothing.views.cart', name='cart'),
    # url(r'^search/$', 'clothing.views.search', name='search'),
    # url(r'^about/', 'clothing.views.about', name='about'),
    # url(r'^cart/add/', 'clothing.views.addToCart', name='addToCart'),
    url(r'^accounts/register/$', 'clothing.views.custom_registration', name='register'),

    # url(r'^dashboard/', 'clothing.views.dashboard', name='dashboard'),
    # url(r'^like_product/', 'clothing.views.like_product', name='like_product'),
    
    url(r'^accounts/login/$', login_forbidden(login), name="login"),
    # url(r'^accounts/login/$', 'clothing.views.custom_login', name='auth_login'),
    # url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), )