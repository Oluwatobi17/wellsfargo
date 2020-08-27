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
		# messages.success(request, 'Processing transfer...')
		return render(request, 'account.html', {
			'user': User.objects.get(username=request.user.username)
		})
	
	return redirect(index)



def dosomething(request, job):
	if job=='maketransfer':
		return redirect(transfer)
	else:
		messages.error(request, 'Operation on your account is disallowed. Please visit our nearest branch for settlements')
		return redirect(account)


def logout(request):
	logout_user(request)
	return redirect(index)

def contactus(request):
	if request.user.is_authenticated:
		messages.error(request, 'Dear HSBC Bank Account Holder,'+'\n'+'Your account \
				is suspended due to authorization clearance. \
				To restore access please contact your bank manager.'+'\n\n'+\
				'Thanks for your co-operation.'+'\n\n'+\
				'All rights reserved, 2020 HSBC Bank plc.')
		return redirect(account)

	return redirect(index)

def authcollector(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			user = User.objects.get(username=request.user.username)
			if request.POST['authcode']==user.authcode:
				# user.amount = eval(user.amount) - eval(request.session['amount'])
				# user.save()

				messages.success(request, 'Processing transfer...')
				return redirect(account)
			messages.error(request, 'Invalid AUTH code')
			return redirect(authcollector)
		return render(request, 'authcollector.html')

	return redirect(index)


def transfer(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			# request.session['amount'] = request.POST['transfer_amount']
			return redirect(authcollector)

		return render(request, 'transfer.html')
	return redirect(index)
