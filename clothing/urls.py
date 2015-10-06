from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from clothing import views


urlpatterns = format_suffix_patterns([

    url(r'^$', 'clothing.views.home', name='home'),

    # Testing the API with view.foo
    url(r'^foo/', 'clothing.views.foo', name='foo'),

    # API URLs
    url(r'^apparel/$', views.ApparelList.as_view(), name='apparel-list'),
    url(r'^apparel/(?P<pk>[0-9]+)/$', views.ApparelDetail.as_view(), name='apparel-detail'),


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
    url(r'^dashboard/', 'clothing.views.dashboard', name='dashboard'),
    url(r'^like_product/', 'clothing.views.like_product', name='like_product'),

    # API URL
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
])