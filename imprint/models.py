from django.db import models

# Create your models here.
class Home(models.Model):
    home_image1 = models.ImageField(upload_to='pics')
    home_image2 = models.ImageField(upload_to='pics')
    home_desc1 = models.TextField()
    home_desc2 = models.TextField()
    home_good_experiance_image = models.ImageField(upload_to='pics')

class Welcome(models.Model):
    welcome_note = models.TextField()

class Inspire(models.Model):
    image= models.ImageField(upload_to='pics')
    description = models.TextField()
    desc_heading = models.CharField(max_length= 100)

class Syas_about_us(models.Model):
    description = models.TextField()
    Student_name = models.CharField
    Student_image = models.ImageField(upload_to='pics')


class Teachers(models.Model):
    teacher_image = models.ImageField(upload_to='pics')
    teacher_name = models.CharField(max_length= 100)
    teacher_subject = models.CharField(max_length= 100)
    teacher_info = models.CharField(max_length= 100)
    teacher_message = models.TextField()
    teacher_back_img = models.ImageField(upload_to='pics')

class Price(models.Model):
    course_heading = models.CharField(max_length=100)
    course_price = models.IntegerField()
    offer_percent = models.IntegerField()
    register_before = models.CharField(max_length=100)
    offer_price = models.IntegerField()
    offer = models.BooleanField(default=False)
    course_image = models.ImageField(upload_to='pics')
    course_description = models.TextField()
    price_back_img = models.ImageField(upload_to='pics')

class Contact(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    num = models.IntegerField()
    contact_back_img = models.ImageField(upload_to='pics')

class Student_info(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    phone = models.IntegerField()
