from django.conf.urls import patterns, url, include
from . import views


urlpatterns = patterns('',

    url(r'^$', views.home, name='home'),
    url(r'^department/(?P<department_slug>[\w\-]+)/$', views.department, name='department'),
    url(r'^department/(?P<department_slug>[\w\-]+)/category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
    url(r'^department/(?P<department_slug>[\w\-]+)/(?P<product_slug>[\w\-]+)/$', views.product, name='product'),
    url(r'^stores/', views.Stores.as_view(), name='stores'),
    url(r'^store/(?P<store>[\w\-]+)/$', views.store, name='store'),
    url(r'^search/$', views.search, name='search'),
    url(r'^about/', views.about, name='about'),
)