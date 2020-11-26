from django.shortcuts import render
from django.http import HttpResponse
from .models import Register

# Create your views here.
def register(request):
    register = Register()
    register.register_image = 'bg_5.jpg'
    register.register_heading = "register"
    register.register_desc = "register here"

    return render(request,'register.html',{'register': register})
 
