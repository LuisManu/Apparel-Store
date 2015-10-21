from django.conf.urls import patterns, url, include











































































# from django.contrib.auth.views import login
# from django.contrib.auth.decorators import user_passes_test


# from .views import custom_registration

# login_forbidden =  user_passes_test(lambda u: u.is_anonymous(), '/')


# urlpatterns = patterns(
#     url(r'^accounts/register/$', custom_registration, name='register'),

#     # url(r'^dashboard/', 'clothing.views.dashboard', name='dashboard'),
#     # url(r'^like_product/', 'clothing.views.like_product', name='like_product'),
    
#     url(r'^accounts/login/$', login_forbidden(login), name="login"),
#     # url(r'^accounts/login/$', 'clothing.views.custom_login', name='auth_login'),
#     # url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
#     url(r'^accounts/', include('django.contrib.auth.urls')),
#     # url(r'^accounts/', include('registration.backends.default.urls')),
# )