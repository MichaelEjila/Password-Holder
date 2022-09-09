from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.urls import reverse
from django.contrib.auth.models import User, auth
from .models import UserData, AccountDetails

from rest_framework.authtoken.models import Token

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


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
	print(details)
	return render(response, 'main/view.html', {"user_data":user_data, "details":details})

def pdf(response):

	user = User.objects.get(username=response.user.username)

	user_data = UserData.objects.get(name = user)
	details = AccountDetails.objects.filter(username=user_data)

	buf = io.BytesIO()

	c = canvas.Canvas(buf, pagesize=letter, bottomup=0 )

	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)


	lines = []
	
	for detail in details:
		lines.append('Username: ' + str(detail.username))
		lines.append('Website: ' + str(detail.website))
		lines.append('Login Info: ' + str(detail.logindetail))
		lines.append('')
		

	for line in lines:
		textob.textLine(line)

	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	return FileResponse(buf, as_attachment=True, filename= 'data.pdf ')

 
def apitoken(request):
	user = User.objects.get(username=request.user.username)
	token = Token.objects.get(user=user)
	return render(request, 'main/apitoken.html', {"token":token})