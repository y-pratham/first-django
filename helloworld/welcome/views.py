from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)

def hobbies(request):
	context = {}
	template = 'task1.html'
	return render(request,template,context)

def apps(request):
	context = {}
	template = 'mycalculator.html'
	return render(request,template,context)