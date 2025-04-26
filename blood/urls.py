from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), 

   
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/approve_request/<int:request_id>/', views.approve_request, name='approve_request'),
    path('admin-panel/delete_request/<int:request_id>/', views.delete_request, name='delete_request'),
    path('admin-panel/delete_donor/<int:donor_id>/', views.delete_donor, name='delete_donor'),
    path('send-otp/', views.send_otp, name='send_otp'),
    path('verify/', views.verify_otp, name='verify_otp'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('',views.index, name='index'),

    path('motive/', views.motive, name='motive'),
    path('approve_donor_for_request/<int:donor_id>/<int:request_id>/', views.approve_donor_for_request, name='approve_donor_for_request'),
    path('approve_request/<int:request_id>/', views.approve_request, name='approve_request'), 
    path('index/', views.index, name='index'),
    path('requestforblood/', views.request_for_blood, name='request_for_blood'),
     path('registerasdonor/', views.register_as_donor, name='register_as_donor'),
    path('registerasdonor/success/', views.register_as_donor_success, name='register_as_donor_success'),path('contactus/', views.contact, name='contactus'),
    
    path('thanks/', views.thanks, name='thanks'),  
    path('feedback/', views.feedback_view, name='feedback'), 
    path('thanks_feedback/', views.thanks_feedback, name='thanks_feedback'),
    path('request_success/', views.success, name='success'),
    path('delete_feedback/<int:id>/', views.delete_feedback, name='delete_feedback'),
    path('delete_contact_us/<int:id>/', views.delete_contact_us, name='delete_contact_us'),
    path('show_matched_donors/<int:request_id>/', views.show_matched_donors, name='show_matched_donors'),

]
