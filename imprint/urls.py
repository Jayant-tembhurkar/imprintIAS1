from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('teacher/',views.teacher, name='teacher'),
    path('pricing/',views.pricing, name='pricing'),   
    path('contact/',views.contact, name='contact'),
    path('base/',views.base, name='base')

]
