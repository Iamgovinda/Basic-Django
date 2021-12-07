from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'home.html',{'name': input("Enter your name: ")})

def add(request):

    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    res=val1+val2
    return render(request,'Result.html',{'Result':res})