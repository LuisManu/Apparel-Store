from django.shortcuts import render
from django.http import HttpResponse

from clothing.models import ApparelInfo

from .models import OrderTicket




def add(request):
	product_id = request.GET['product_id']
	product_size = request.GET['size']
	user = request.user

	product = ApparelInfo.objects.get(pk=product_id)
	add_to_cart = OrderTicket(user=user, product_name=product, size=product_size)
	add_to_cart.save()

	user_order_tickets = OrderTicket.objects.filter(user=user)
	cart_count = len(user_order_tickets)
	return HttpResponse(cart_count)


def cart(request):
	user = request.user
	cart_items = OrderTicket.objects.filter(user=user)
	return render(request, 'cart/cart.html', {'cart_items': cart_items})



import json

def to_checkout(request):


	print
	print


	json_cart = request.GET['json_cart']


	print json_cart
	print type(json_cart)


	bar = json.loads(json_cart)
	print
	print
	print type(bar)
	for x in bar:
		print x

	# print
	# print bar[0]['product']
	# print

	print
	print
	foobar = ApparelInfo.objects.get(title=bar[0]['product'])
	foo_size = bar[0]['size']
	print type(foo_size)
	print foo_size
	print
	print
	print getattr(foobar, foo_size)
	# print foobar

	print
	print
	foo	='test check'
	print foo
	return HttpResponse(foo)
