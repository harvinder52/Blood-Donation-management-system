from django.contrib import admin
from .models import Contact, Feedback, Donor, BloodRequest

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'blood_need')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'time_to_contact', 'first_time_donator', 'where_heard_about_us', 'inspiration_to_donate', 'process_easy', 'donate_next_year', 'recommend_to_others', 'age_range')
    list_filter = ('time_to_contact', 'first_time_donator', 'where_heard_about_us', 'process_easy', 'donate_next_year', 'recommend_to_others', 'age_range')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact_number', 'state', 'city', 'address', 'gender', 'blood_group', 'date_of_birth')
    list_filter = ('state', 'city', 'gender', 'blood_group')
    search_fields = ('first_name', 'last_name', 'email', 'contact_number', 'address')

@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'state', 'city', 'contact_number', 'address', 'blood_group', 'date_of_birth')
    list_filter = ('state', 'city', 'blood_group')
    search_fields = ('full_name', 'email', 'contact_number', 'address')
