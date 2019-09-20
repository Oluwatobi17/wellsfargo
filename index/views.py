from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib import messages
from .models import User


def index(request):
	if request.method=='POST':
		username = request.POST['j_username']
		password = request.POST['j_password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			if user.is_active:
				login_user(request, user)
				return redirect(account)

			messages.error(request, 'Your account has been disabled')
			return redirect(index)
		
		return redirect(index)

	return render(request, 'index.html')

# 
#password: linda1273
#Username: Linda89 

def account(request):
	if request.user.is_authenticated:
		return render(request, 'account.html', {
			'user': User.objects.get(username=request.user.username)
		})
		
	return redirect(index)



def dosomething(request, job):
	if job=='maketransfer':
		messages.error(request, 'Operation on your account is disallowed especially transfer. Please visit our nearest branch for settlements')
		return redirect(account)
	else:
		messages.error(request, 'Operation on your account is disallowed. Please visit our nearest branch for settlements')
		return redirect(account)


def logout(request):
	logout_user(request)
	return redirect(index)