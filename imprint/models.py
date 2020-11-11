from django.db import models

# Create your models here.
class Home:
    home_image1 = str
    home_image2 = str
    home_desc1 = str
    home_desc2 = str
    home_good_experiance_image = str
    home_quote_image = str

class Welcome:
    welcome_note = str

class Inspire:
    image: str
    description : str
    desc_heading : str

class Syas_about_us:
    description = str
    Student_name = str
    Student_image = str


class Teachers:
    id : int
    teacher_image : str
    teacher_name : str
    teacher_subject: str
    teacher_info :str
    teacher_message : str
    teacher_back_img : str

class Price:
    id : int
    course_heading : str
    course_price : int
    offer_percent : int
    register_before : str
    offer_price : int
    offer : bool
    course_image : str
    course_description : str
    price_back_img : str

class Contact:
    id : int
    title : str
    address : str
    num : str   
    contact_back_img : str

class Student_info:
    first_name = str
    last_name = str
    course = str
    phone = int
    message = str
