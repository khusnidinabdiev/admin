from django.urls import path
from . import views



urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('products', views.products, name='projects'),
	path('customer', views.customer, name='customer')

]