from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dashboard(request):
	return render(request, 'welcome/dashboard.html')


def products(request):
	return render(request, 'welcome/products.html')


def customer(request):
	return render(request, 'welcome/customer.html')


