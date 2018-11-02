from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Customer, Manager, Restaurant, Item, Order
import datetime
import pdfkit
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def customer_signup(request):
	if request.method == "POST":
		cust_id = request.POST['cust_id']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		user = User(username=username, first_name=first_name, last_name=last_name, email=email, user_type=2)
		user.set_password(password)
		user.save()
		customer = Customer(cust_id=cust_id, user=user)
		customer.save()
		return redirect('customer_home', pk=customer.cust_id)
	else:
		return render(request, 'customer_signup.html')

def customer_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.user_type == 2:
                    login(request, user)
                    return redirect('customer_home') #, pk=user.security.id)
                else:
                    return render(request, 'customer_login.html', {'error_message': 'Invalid security staff credentials'})
            else:
                return render(request, 'customer_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'customer_login.html', {'error_message': 'Invalid login'})
    return render(request, 'customer_login.html')

def customer_home(request,pk):
	customer = get_object_or_404(Customer, pk=pk)
	return render(request, 'customer_home.html', {'customer': customer})

def home(request):
	return render(request, 'home.html')