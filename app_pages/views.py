from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bosh_sahiyfa(request):
    return render(request, 'index5.html')
def python(request):
    return render(request, 'index1.html')

def java(request):
    return render(request ,'index2.html')

def django(request):
    
    return render(request,'index.html')

def cpp(request):
    
    return render(request,'index3.html')

def go (request):
    
    return render(request, 'index4.html')
