from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page

from rest_framework import generics

from .serializers import ApparelSerializer, CategorySerializer, DepartmentSerializer
from .models import ApparelInfo, Category, Department, Store, CarouselImage, UserProfile
from .search import get_query
from .forms import UserCreateForm, CustomLoginForm

# def custom_login(request):
# 	if request.method == "POST":
# 		form = CustomLoginForm(request.POST)
# 		print
# 		print
# 		print request.POST.get('username')
# 		print request.POST.get('password')
# 		print
# 		print
# 		username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return HttpResponseRedirect('/dashboard/')
#     else:
# 		form = CustomLoginForm
# 		return render(request, 'registration/login.html', {'form': form})


class ApparelList(generics.ListCreateAPIView):
	queryset = ApparelInfo.objects.all()
	serializer_class = ApparelSerializer



class ApparelDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = ApparelInfo.objects.all()
	serializer_class = ApparelSerializer
	template_name = 'jsontest.html'


def foo(request):
	return render(request, 'jsontest.html')




# def custom_login(request):
# 	if request.user.is_authenticated():
# 		return HttpResponseRedirect('/')
# 	else:
# 		if request.method == 'POST':
# 		    username = request.POST['username']
# 		    password = request.POST['password']
# 		    user = authenticate(username=username, password=password)
# 		    login(request, user)
# 		    # if user:
# 		    #     if user.is_active:
# 		    #         login(request, user)
# 			return HttpResponseRedirect('/clothing/dashboard/')
# 		else:
# 			form = AuthenticationForm
# 			return render(request, 'registration/login.html', {'form': form})

def custom_registration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	elif request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, new_user)
			return HttpResponseRedirect('/dashboard/')
	else:
		form = UserCreateForm()
	return render(request, 'registration/registration_form.html', {'form': form})


def home(request):
	carousel_images = CarouselImage.objects.all()
	first_img = carousel_images[0]
	carousel_imgs =[]


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







@cache_page(60 * 15)
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


	'''
	create algorithm that uses current product, and user likes(product category likes category, product department likes department) to
	show suggestions.
	'''

	# print
	# print
	# print userprofile.likes.all()
	# print
	# print
	return render(request, 'clothing/product.html', context_dict)








def stores(request):
	stores = Store.objects.all()
	return render(request, 'stores.html', {'stores': stores})


def store(request, store):
	store = Store.objects.get(slug=store)
	return render(request, 'store.html', {'store': store})


def cart(request):
	return render(request, 'cart.html')
	


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







@csrf_protect
def testing(request):
	'''
	THIS CODE HAS BEEN MOVED TO custom_registration.

	Creating a User, UserProfile, authenticating, and logging in. Works! Sweet!

	Used django.contrib.auth.forms import UserCreationForm in UserCreateForm in forms.py.

	Made UserCreateForm (custom form) to mixin email and UserProfile model.

	'''
	if request.method == 'POST':
		userform = UserCreateForm(request.POST)
		if userform.is_valid():
			userform.save()
			new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, new_user)
			return HttpResponseRedirect('/dashboard/')
	else:
		userform = UserCreateForm()
	return render(request, 'testing.html', {'userform': userform})










@login_required
def dashboard(request):
	user = User.objects.get(username=request.user.username)
	userprofile = UserProfile.objects.get(user=user)

	# userprofile.likes.remove(ApparelInfo.objects.get(title="A WHOLE NEW WORLD LEGGINGS"))
	# art.publications.remove(Publication.objects.get(title="awesome"))


	# print
	# print
	# for like in userprofile.likes.all():
	# 	print 1
	# print
	# print


	if len(userprofile.likes.all()) < 3:
		messages.info(request, 'Start liking clothing')

	context = {'user': user, 'userprofile': userprofile}
	return render(request, 'dashboard.html', context)





import json

@login_required
def like_product(request):
	user = User.objects.get(username=request.user.username)
	userprofile = UserProfile.objects.get(user=user)

	product_id = None
	if request.method == 'GET':
		product_id = request.GET['product_id']

	if product_id:
		product = ApparelInfo.objects.get(id=int(product_id))
		if product not in userprofile.likes.all():
			userprofile.likes.add(ApparelInfo.objects.get(title=product))
			likes_counter = product.likes_counter + 1
			product.likes_counter = likes_counter
			product.save()
			userprofile.save()

			user_likes = userprofile.likes.all()
			foo = {'user_likes': str(user_likes), 'likes_counter': str(likes_counter)}
			foo_p = json.dumps(foo, ensure_ascii=False)

			return HttpResponse(foo_p)
		else:
			userprofile.likes.remove(ApparelInfo.objects.get(title=product))
			likes_counter = product.likes_counter - 1
			product.likes_counter = likes_counter
			product.save()
			userprofile.save()

			user_likes = userprofile.likes.all()
			foo = {'user_likes': str(user_likes), 'likes_counter': str(likes_counter)}
			foo_p = json.dumps(foo, ensure_ascii=False)
			return HttpResponse(foo_p)

	# return HttpResponse(likes_counter, user_likes)
	# return render(request)








from registration.backends.simple.views import RegistrationView

# from clothing.models import UserProfile

class MyRegistrationView(RegistrationView):
	'''
	This has been depricated. Works. Can be used with Django-registration-redux or UserCreateForm(UserCreationForm):

	'''
	def get_success_url(self,request, user):
		user = request.user
		userprofile = UserProfile(user=user)
		userprofile.save()
		return '/dashboard/'