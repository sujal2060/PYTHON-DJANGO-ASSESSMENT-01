from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def homeview(request):
    return render(request,'info/index.html')
def aboutview(request):
    return render(request,'info/about.html')
def contactview(request):
    return render(request,'info/contact.html')
def loginview(request):
    return render(request,'info/login.html')
def registerview(request):
    return render(request,'info/register.html')