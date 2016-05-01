import json

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from apps.clothing.models import ApparelInfo

from .forms import UserCreateForm
from .models import UserProfile




def custom_registration(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	elif request.method == 'POST':
		form = UserCreateForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			new_user = authenticate(username=username, password=password)
			login(request, new_user)
			return HttpResponseRedirect('/accounts/dashboard/')
	else:
		form = UserCreateForm()
	return render(request, 'registration/registration_form.html', {'form': form})


@login_required
def dashboard(request):
	user = User.objects.get(username=request.user.username)
	userprofile = UserProfile.objects.get(user=user)

	if len(userprofile.likes.all()) < 3:
		messages.info(request, 'Start liking clothing')

	context = {'user': user, 'userprofile': userprofile}
	return render(request, 'dashboard.html', context)


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