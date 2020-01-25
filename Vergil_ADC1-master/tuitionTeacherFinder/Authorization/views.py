from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from teacherprofile.models import UserInfo


def home(request):
	return render(request, 'Authorization/home.html', )

def register(request):
	return render(request, 'Authorization/register.html', )

def registerForm(request):
	if request.method == 'POST':
		print('Hello')
		first_name= request.POST['first_name']
		last_name= request.POST['last_name']
		username= request.POST['username']
		email= request.POST['email']
		user_type= request.POST['user_type']
		password1= request.POST['password1']
		password2= request.POST['password2']
		user= User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
		user.save();
		UserInfo.objects.create(user_type=user_type, users_id=user.id)
		print('User created')
		return HttpResponse('Pass')
	else:
		return HttpResponse('FAiled')
		# return render(request,'Accounts/register.html', )

def loginForm(request):
		username= request.POST['username']
		password= request.POST['password1']
		
		user= auth.authenticate(username=username, password=password)
		return HttpResponse('Welcome')

def login(request):
	return render(request,'Authorization/login.html', ) 

def logout():
	return 