from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
	return render(request, 'index.html')