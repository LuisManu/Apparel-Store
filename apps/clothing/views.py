from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView

from apps.auth_app.models import UserProfile

from .models import ApparelInfo, Category, Department, Store, CarouselImage
from .search import get_query





def home(request):
	carousel_images = CarouselImage.objects.all()
	first_img = carousel_images[0]
	carousel_imgs = []

	for img in carousel_images:
		if img == first_img:
			pass
		else:
			carousel_imgs.append(img)

	carousel_len = range(len(carousel_imgs))
	carousel_nums = []

	for num in carousel_len:
		carousel_nums.append(num+1)

	context_dict = {
		'carousel_images': carousel_images,
		'first_img': first_img,
		'carousel_imgs': carousel_imgs,
		'carousel_nums': carousel_nums
	}
	return render(request, 'clothing/home.html', context_dict)




def department(request, department_slug):
	department = Department.objects.get(slug=department_slug)
	apparel_items = ApparelInfo.objects.filter(department=department).order_by('-date_time')
	cats = []

	for product in apparel_items:
		if str(product.category) in cats:
			pass
		else:
			cats.append(str(product.category))

	paginator = Paginator(apparel_items, 24)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	context_dict = {'products': products, 'department': department, 'cats': sorted(cats)}
	return render(request, 'clothing/department.html', context_dict)




def category(request, department_slug, category_name_slug):
	department = Department.objects.get(slug=department_slug)
	category = Category.objects.get(slug=category_name_slug)
	for_nav = ApparelInfo.objects.filter(department=department)
	cats = []

	for product in for_nav:		
		if str(product.category) in cats:
			pass
		else:
			cats.append(str(product.category))

	apparel_items = ApparelInfo.objects.filter(department=department).filter(category=category)
	paginator = Paginator(apparel_items, 24)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)

	categories = Category.objects.all()
	context_dict = {'category': category, 'products': products, 'cats': sorted(cats), 'department': department}

	return render(request, 'clothing/department.html', context_dict)




def product(request, department_slug, product_slug):
	product = ApparelInfo.objects.get(slug=product_slug)

	if request.user.is_authenticated():
		user = User.objects.get(username=request.user)
		userprofile = UserProfile.objects.get(user=user)

	area_image = product.image

	image_list = []
	if product.image2:
		image_list.append(product.image2)
	if product.image3:
		image_list.append(product.image3)
	if product.image4:
		image_list.append(product.image4)
	if product.image5:
		image_list.append(product.image5)

	sizes = [
		product.xsmall,
		product.small,
		product.medium,
		product.large,
		product.xlarge
	]

	area_image_len = len([area_image])
	image_list_len = len(image_list)
	img_nums = range(area_image_len + image_list_len)

	image_nums = []
	carousel_counter = []

	for num in img_nums:
		image_nums.append(num+1)
	image_nums.pop(-1)

	context_dict = {}
	context_dict = {
		'product': product,
		'area_image': area_image,
		'image_list': image_list,
		'sizes': sizes,
		'image_nums': image_nums
	}

	if request.user.is_authenticated():
		context_dict['userprofile'] = userprofile
		context_dict['user_likes'] = userprofile.likes.all()

	return render(request, 'clothing/product.html', context_dict)




class Stores(ListView):
	template_name = 'clothing/stores.html'
	context_object_name = 'stores'

	def get_queryset(self):
		return Store.objects.all()




def store(request, store):
	store = Store.objects.get(slug=store)
	return render(request, 'clothing/store.html', {'store': store})




def search(request):
    query_string = ''
    found_entries = None
    # cat = ApparelInfo.objects.all()
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = get_query(query_string, [
        	'title',
        	'brand', 'price', 'description'
        	])
        found_entries = ApparelInfo.objects.filter(entry_query)
    return render(request, 'search.html',
                          {'query_string': query_string, 'found_entries': found_entries})




def about(request):
	stores = Store.objects.all()
	return render(request, 'clothing/about.html', {'stores': stores})