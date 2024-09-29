from django.shortcuts import render
from django.http import HttpResponse

def index(request):
# should access model objects and use Templated to prepare responses.
   
   return HttpResponse('Hello World')

# Create your views here.

