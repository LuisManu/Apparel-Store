from django.conf.urls import patterns, include, url
from cart import views





urlpatterns = patterns('',
	url(r'^add/', 'cart.views.add', name='add'),
	url(r'^cart/', views.cart, name='cart'),
	url(r'^to-checkout/', views.to_checkout, name='checkout'),
)