import json

from django.shortcuts import render
from django.http import HttpResponse

from apps.clothing.models import ApparelInfo

from .models import ItemInCart, ToBeShipped




def add(request):
	product_id = request.GET['product_id']
	product_size = request.GET['size']
	user = request.user

	product = ApparelInfo.objects.get(pk=product_id)
	add_to_cart = ItemInCart(user=user, product_name=product, size=product_size)
	add_to_cart.save()

	user_order_tickets = ItemInCart.objects.filter(user=user)
	cart_count = len(user_order_tickets)
	return HttpResponse(cart_count)


def cart(request):
	user = request.user
	cart_items = ItemInCart.objects.filter(user=user)
	return render(request, 'cart/cart.html', {'cart_items': cart_items})


def to_checkout(request):
	in_cart = request.GET['in_cart']
	json_cart = json.loads(in_cart)
	to_shipping = []
	user = request.user

	for item in json_cart:
		product = ApparelInfo.objects.get(title=item['product'])
		size = item['size']
		size_check = getattr(product, size)

		if size_check > 0:
			foo_dict = {}
			foo_dict['product'] = product
			foo_dict['size'] = size
			foo_dict['price'] = product.price
			to_shipping.append(foo_dict)
			del_item_in_cart = ItemInCart.objects.get(product_name=product)
			del_item_in_cart.delete()

	to_be_shipped = ToBeShipped(user=user, items_to_be_shipped=to_shipping)
	to_be_shipped.save()
	foo	='test check'

	return HttpResponse(foo)