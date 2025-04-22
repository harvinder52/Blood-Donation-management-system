from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('',views.login,name='login.html') ,
    path('registration/',views.registed,name='registration.html') ,
    path('motive/', views.motive, name='motive.html'),
    path('index/', views.index, name='index.html'),
    path('requestforblood/', views.request_for_blood, name='requestforblood.html'),
    path('seeallrequest/', views.see_all_request, name='seeallrequest.html'),
    path('registerasdonor/', views.register_as_donor, name='registerasdonor.html'),
    path('contactus/', views.contact, name='contactus.html'),
    path('feedback/', views.feedback, name='feedback.html'),
    path('thanks/', views.thanks, name='thanks.html'),  
    path('feedback/', views.feedback, name='feedback.html'), 
    path('thanks_feedback/', views.thanks_feedback, name='thanks_feedback.html'),
    path('request_success/', views.success, name='success.html')
]
