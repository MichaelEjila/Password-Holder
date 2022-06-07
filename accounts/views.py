from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from main.models import UserData

#Email imports
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def register(request):
	if request.method == "POST":
		full_name = request.POST['fullname']
		username = request.POST['username']
		pwd1 = request.POST['password1']
		pwd2 = request.POST['password2']

		if (pwd1 == pwd2):	
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username taken')
				return redirect('/register')


			user = User.objects.create_user(username=username, password=pwd2)
			user.save();
			new = UserData(name=username, slug = username)
			new.save();
			return redirect('/login')
		else:
			messages.info(request, 'Password does not match')
			return redirect('/register')


		
	else:
		return render(request, 'accounts/register.html', {})

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')

		else:
			messages.info(request, 'Invalid Login Details')
			return redirect('/login')

	return render(request, 'accounts/login.html', {})

def logout(request):
	auth.logout(request)
	return redirect('/')
	return HttpResponse("Logout Page")
