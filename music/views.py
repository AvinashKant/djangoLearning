from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Album


def home(request):
	return HttpResponse("welcome")

def index(request):
	all_album = Album.objects.all()
	template = loader.get_template('hello.html')
	html = ''
	context = {"avinash":'avinash'}
	return HttpResponse(template.render(context,request))

def rendermethod(request):
	context = {"avinash":'avinash kant'}
	return render(request,'hello.html',context)

def pagenotfound(request):
	raise Http404('Album not found ha ha')

def first(request):
	return HttpResponse("sad")

def firstaa(request):
	return HttpResponse("sad brp")