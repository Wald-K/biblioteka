from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from biblioteka import settings
from django.urls import reverse


# Create your views here.
def Login(request):
	next = request.GET.get('next', reverse('bookrent:index'))     #'/bookrent/')  
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username= username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				return HttpResponse('Inactive user')
		else:
			HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, 'accounts/login.html', {'redirect_to':next})

def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)


