from django.conf.urls import  url
from django.contrib.auth import views as auth_view
from . views import Login, Logout

urlpatterns = [
	#url(r'^login/$',auth_view.login, name='login'),
	#url(r'^login/$',auth_view.login, name='login', kwargs={'template_name': 'accounts/login.html'}),
	#url(r'^logout/$',auth_view.logout, name='logout', kwargs={'next_page': '/'}),
	url(r'^login/$',Login, name='login'),
	url(r'^logout/$',Logout, name='logout'),
	#url(r'^home/$',views.login, name='login'),
	#url(r'^blog/$',views.login, name='login'),

]