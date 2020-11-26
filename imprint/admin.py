from django.contrib import admin
from django.utils.functional import Promise
from .models import Teachers, Price, Contact, Home, Syas_about_us, Welcome, Inspire 

# Register your models here.
admin.site.register(Teachers)
admin.site.register(Price)
admin.site.register(Contact)
admin.site.register(Home)
admin.site.register(Syas_about_us)
admin.site.register(Welcome)
admin.site.register(Inspire)