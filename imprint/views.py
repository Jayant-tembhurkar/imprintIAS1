from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Teachers, Price, Contact, Home, Syas_about_us, Welcome, Inspire


# Create your views here.

def index(request):
    
    home = Home.objects.all()
    inspi = Inspire.objects.all()  
    wel = Welcome.objects.all()
    says = Syas_about_us.objects.all()

    return render(request,'index.html', {'home':home, 'say': says, 'welc':wel, 'inspire': inspi })

def teacher(request):
    teacher = Teachers.objects.all()
    return render(request,'teacher.html',{'teach':teacher})

def pricing(request):
    price = Price.objects.all()
    return render(request,'pricing.html', {'course':price})

def contact(request):
    contact = Contact.objects.all()
    return render(request,'contact.html',{'contact': contact})

def base(request):
    return render(request,'base.html')