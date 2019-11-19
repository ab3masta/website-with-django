from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')

def contact(request):
    return render(request,'pages/contact.html')  
    
def exemple1(request):
    return render(request,'pages/exemple1.html') 

def handler404(request,exception):
    return render(request,'errors/404.html',{'error': exception},status=404)
           
def handler500(request,exception=None):
    return render(request,'errors/500.html',{},status=500)    