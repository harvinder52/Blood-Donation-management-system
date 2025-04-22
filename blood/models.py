from django.db import models

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
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=100)

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