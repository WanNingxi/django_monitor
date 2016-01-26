from django.shortcuts import render_to_response
from polls.models import IP_address, status 
from django.http import HttpResponse

# Create your views here.


def monitor(request):
	IP_addresses = IP_address.objects.all()
	return render_to_response('index.html',{'IP_addresses':IP_addresses})



def index(request):
	return HttpResponse('wanningxi')
