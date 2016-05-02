from django.conf.urls import patterns, include, url
from . import views



urlpatterns = patterns('',
	url(r'^add/', views.add, name='add'),
	url(r'^cart/', views.cart, name='cart'),
	url(r'^to-checkout/', views.to_checkout, name='checkout'),
)