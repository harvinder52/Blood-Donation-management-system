from django.contrib import admin
from .models import Contact, Feedback, Donor, BloodRequest

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'blood_need')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'rating', 'submitted_at')  # Keep only the fields in the model
    list_filter = ('rating', 'submitted_at')  # Use existing fields for filtering

admin.site.register(Feedback, FeedbackAdmin)
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
