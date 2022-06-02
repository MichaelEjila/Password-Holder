from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from .models import UserData, AccountDetails

# Create your views here
def index(request):
	return render(request, 'main/base.html', {})

def create(request):
	user = User.objects.get(username=request.user.username)
	if request.method == 'POST':
		website = request.POST['website']
		logindetail = request.POST['logindetail']
		password = request.POST['password']


		user_name = UserData.objects.get(name= user)
		account = AccountDetails(user=user_name, username=user, website=website, logindetail=logindetail, password=password)
		account.save();
		return HttpResponseRedirect(reverse('view'))
	return render(request, 'main/create.html', {})

def view(response):
	user = User.objects.get(username=response.user.username)

	user_data = UserData.objects.get(name = user)
	details = AccountDetails.objects.filter(username=user_data)
	return render(response, 'main/view.html', {"user_data":user_data, "details":details})