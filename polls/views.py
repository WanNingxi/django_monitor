from django.shortcuts import render_to_response
from polls.models import Author, Book
from django.http import HttpResponse

# Create your views here.


def show_author(request):
	authors = Author.objects.all()
	return render_to_response('index.html',{'authors':authors})



def index(request):
	return HttpResponse('wanningxi')
