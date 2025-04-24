from django.db import models
from django.shortcuts import render
from django.utils import timezone
import uuid

class User(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

class EmailOTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email} - {self.otp}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    blood_need = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    time_to_contact = models.CharField(max_length=20)
    first_time_donator = models.CharField(max_length=3)
    where_heard_about_us = models.CharField(max_length=50)
    inspiration_to_donate = models.CharField(max_length=100)
    process_easy = models.CharField(max_length=3) 
    donate_next_year = models.CharField(max_length=3)
    recommend_to_others = models.CharField(max_length=3)
    improve_experience = models.TextField()
    improve_utilization = models.TextField()
    age_range = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Donor(models.Model):
    BLOOD_CHOICES = [
        ('A', 'A+'),
        ('A−', 'A−'),
        ('B+', 'B+'),
        ('B−', 'B−'),
        ('AB+', 'AB+'),
        ('AB−', 'AB−'),
        ('O+', 'O+'),
        ('O−', 'O−')
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15, null=False, default='0000000000')  # Provide a default value
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)  # Keep nullable (optional)
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')])
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BloodRequest(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    blood_group = models.CharField(max_length=10)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.full_name

class loginform(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class registerform(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=100)
    bloodtype=models.CharField(max_length=100)

    def __str__(self):
        return self.email
    

def admin_dashboard(request):
    blood_requests = BloodRequest.objects.all().order_by('-request_date')
    donors = Donor.objects.all().order_by('-registered_on')  # adjust field names as per your model
    return render(request, 'admin_dashboard.html', {
        'blood_requests': blood_requests,
        'donors': donors,
    })
