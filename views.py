from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
	return HttpResponse("Hello world!")


def home_page(request):

	print(request.method)
	
	return render(request,"index.html")