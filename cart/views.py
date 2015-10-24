from django.shortcuts import render
from django.http import HttpResponse

from clothing.models import ApparelInfo

from .models import OrderTicket




def add(request):
	product_id = request.GET['product_id']
	product_size = request.GET['size']
	user = request.user

	# print
	# print user
	# print
	
	product = ApparelInfo.objects.get(pk=product_id)
	add_to_cart = OrderTicket(user=user, product_name=product, size=product_size)
	add_to_cart.save()


	user_order_tickets = OrderTicket.objects.filter(user=user)



	cart_count = len(user_order_tickets)

	foo = 'hello there check'
	print foo
	return HttpResponse(cart_count)


def cart(request):
	user = request.user
	cart_items = OrderTicket.objects.filter(user=user)
	return render(request, 'cart/cart.html', {'cart_items': cart_items})
