from django.conf.urls import patterns, include, url

from django.contrib.auth.views import login
from django.contrib.auth.decorators import user_passes_test
from views import custom_registration, dashboard, like_product

login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/')


urlpatterns = patterns('',
    url(r'^register/$', custom_registration, name='register'),
    url(r'^login/$', login_forbidden(login), name="login"),
    url(r'^dashboard/', dashboard, name='dashboard'),
    url(r'^like_product/', like_product, name='like_product'),
    # url(r'^accounts/custom_login/$', custom_login, name='custom_login'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^accounts/', include('registration.backends.default.urls')),
)