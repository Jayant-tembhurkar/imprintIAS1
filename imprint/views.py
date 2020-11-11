from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Teachers, Price, Contact, Home, Syas_about_us, Welcome, Inspire, Student_info


# Create your views here.

def index(request):
    home = Home()
    home.home_image1 = 'bg_1.jpg'
    home.home_image2 = 'bg_2.jpg'
    home.home_desc1 = 'we are going \n to make it...'.title()
    home.home_desc2 = 'Perfect Coaching Institute For MPSC/UPSC'
    home.home_quote_image = 'bg_5.jpg'
    
    inspire = Inspire()
    inspire.image = "bg_3.jpg"
    inspire.desc_heading = "join today"
    inspire.description = "aao baccho tumhe sikhaye"
    
    wel = Welcome()
    wel1 = Welcome()
    wel.welcome_note = 'we are providing our best in it'
    wel1.welcome_note = 'you have to give your best in it'
    welc = [wel, wel1]

    says = Syas_about_us()
    says.description = 'this is the best institute one can must join in it'
    says.Student_name = 'jayant'
    says.Student_image = 'teacher-1.jpg'

    says1 = Syas_about_us()
    says1.description = 'this is the best institute one can must join in it'
    says1.Student_name = 'jayant'
    says1.Student_image = 'teacher-2.jpg'

    says2 = Syas_about_us()
    says2.description = 'this is the best institute one can must join in it'
    says2.Student_name = 'jayant'
    says2.Student_image = 'teacher-3.jpg'

    say = [says,says1,says2]

    

    return render(request,'index.html', {'home':home, 'say': say, 'welc':welc, 'inspire': inspire })

def teacher(request):
    teacher = Teachers()
    teacher.teacher_back_img = "bg_5.jpg"
    teacher1 = Teachers()
    teacher1.teacher_image = 'teacher-1.jpg'
    teacher1.teacher_name = 'shubham'
    teacher1.teacher_subject = 'public administration'
    teacher1.teacher_info = 'he is good at mpsc'
    teacher1.teacher_message = 'Hi there, i am teaching pubad and i promise you guyes after my teaching you will shine in subject'
    
    teacher2 = Teachers()
    teacher2.teacher_image = 'teacher-2.jpg'
    teacher2.teacher_name = 'jayant'
    teacher2.teacher_subject = 'engineering'
    teacher2.teacher_info = 'he is good at upsc'
    teacher2.teacher_message = 'Hi there, i am teaching geography and i promise you guyes after my teaching you will shine in subject'
    
    teacher3 = Teachers()
    teacher3.teacher_image = 'teacher-3.jpg'
    teacher3.teacher_name = 'dip'
    teacher3.teacher_subject = 'genral knowledge'
    teacher3.teacher_info = 'she is good at current affairs'
    teacher3.teacher_message = 'Hi there, i am teaching history and i promise you guyes after my teaching you will shine in subject'
    
    teach = [teacher1, teacher2,teacher3]

    
    return render(request,'teacher.html',{'teach':teach, 'teacher': teacher.teacher_back_img})

def pricing(request):
    price = Price()
    price.price_back_img = "bg_3.jpg"
    price1 = Price()
    price1.register_before = "register before NOV-20"
    price1.offer = False
    price1.offer_percent = 50
    price1.course_heading = 'UPSC'
    price1.course_price = 60000
    price1.offer_price = 30000
    price1.course_image = 'bg_1.jpg'
    price1.course_description = 'In this course we provide ofline lectures of UPSC and library with notes'

    price2 = Price()
    price2.offer = True
    price2.course_heading = 'MPSC'
    price2.register_before = "register before NOV-20"
    price2.offer_percent = 50
    price2.course_price = 50000
    price2.offer_price = 25000
    price2.course_image = 'bg_2.jpg'
    price2.course_description = 'In this course we provide ofline lectures of MPSC and library with notes'

    price3 = Price()
    price3.course_heading = 'UPSC INTIGRATED MPSC'
    price3.register_before = "register before NOV-20"
    price3.offer = True
    price3.offer_percent = 50
    price3.course_price = 80000
    price3.offer_price = 40000
    price3.course_image = 'bg_3.jpg'
    price3.course_description = 'In this course we provide ofline lectures of UPSC & MPSC, library with notes '

    price4 = Price()
    price4.course_heading = 'UPSC OR MPSC TEST SERIES'
    price4.offer = True
    price4.register_before = "register before NOV-20"
    price4.offer_percent = 50
    price4.course_price = 5000
    price4.offer_price = 2500
    price4.course_image = 'bg_4.jpg'
    price4.course_description = 'In this course we provide ofline test series only'

    course = [price1, price2, price3, price4]
    return render(request,'pricing.html', {'course':course,'image':price.price_back_img})

def contact(request):
    contact = Contact()
    contact.contact_back_img = 'bg_2.jpg'
    contact.address = 'The imprint IAS opposit to D.B. science college gondia'
    contact.num = '+91 89754 62358'
    contact.email = 'imprintias1@gmail.com'

    return render(request,'contact.html',{'contact': contact})

def base(request):
    return render(request,'base.html')

