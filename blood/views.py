from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Contact
from .models import Feedback
from .models import Donor
from .models import BloodRequest
from .models import loginform
from .models import registerform

def registed(request):
    if request.method == 'POST':
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Phonenumber=request.POST.get('phonenumber')
        Bloodtype = request.POST.get('bloodtype')
        
        rgn= registerform()
        rgn=name=Name
        rgn.email=Email
        rgn.phonenumber=Phonenumber
        rgn.bloodtype=BloodType
        rgn.save()
        return render(request,'login.html')
    return render(request,'registration.html')

def login(request):
    if request.method == 'POST':
        Username=request.POST.get('username')
        Email = request.POST.get('email')
        Password = request.POST.get('pwd')
        
        lgn = loginform()
        lgn.username=Username
        lgn.email=Email
        lgn.password=Password
        lgn.save()
        return render(request,'index.html')
    return render(request,'login.html')

def motive(request):
    return render(request, 'motive.html')

def index(request):
    return render(request, 'index.html')
def request_for_blood(request):
    if request.method == 'POST':
        
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        state = request.POST.get('state')
        city = request.POST.get('city')
        contact_number = request.POST.get('ContactNumber')
        address = request.POST.get('address')
        blood_group = request.POST.get('bloodgroup')
        date_of_birth = request.POST.get('date_birth')
        blood_request = BloodRequest(
            full_name=full_name,
            email=email,
            state=state,
            city=city,
            contact_number=contact_number,
            address=address,
            blood_group=blood_group,
            date_of_birth=date_of_birth
        )
        blood_request.save()
        return render(request,'success.html')
    return render(request, 'requestforblood.html')

def success(request):
    return render(request, 'success.html')
def see_all_request(request):
    blood_requests = BloodRequest.objects.all()
    return render(request, 'seeallrequest.html', {'blood_requests': blood_requests})

def register_as_donor(request):
    if request.method == 'POST':
        # Retrieve data from the form
        first_name = request.POST.get('FirstName')
        last_name = request.POST.get('LastName')
        email = request.POST.get('Email')
        contact_number = request.POST.get('ContactNumber')
        state = request.POST.get('state')
        city = request.POST.get('city')
        address = request.POST.get('Address')
        gender = request.POST.get('Gender')
        blood_group = request.POST.get('bloodgroup')
        date_of_birth = request.POST.get('date_birth')
        password = request.POST.get('Password')

        # Create a new donor object
        donor = Donor(
            first_name=first_name,
            last_name=last_name,
            email=email,
            contact_number=contact_number,
            state=state,
            city=city,
            address=address,
            gender=gender,
            blood_group=blood_group,
            date_of_birth=date_of_birth,
            password=password
        )
    
        donor.save()
        return render(request, 'thanks.html')
    else:
        return render(request, 'registerasdonor.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('Phoneno')
        blood_need = request.POST.get('blood_need')  
        contact = Contact(name=name, email=email, phone=phone, blood_need=blood_need)
        contact.save()
        return render(request, 'thanks.html')
    return render(request, 'contact.html')

def thanks(request):
    return render(request, 'thanks.html')


def feedback(request):
    if request.method == 'POST':
        # Retrieve data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        time_to_contact = request.POST.get('time_to_contact')
        first_time_donator = request.POST.get('first_time_donator')
        where_heard_about_us = request.POST.get('where_heard_about_us')
        inspiration_to_donate = request.POST.get('inspiration_to_donate')
        process_easy = request.POST.get('process_easy')
        donate_next_year = request.POST.get('donate_next_year')
        recommend_to_others = request.POST.get('recommend_to_others')
        improve_experience = request.POST.get('improve_experience')
        improve_utilization = request.POST.get('improve_utilization')
        age_range = request.POST.get('age_range')

        # Create a new Feedback object and save it to the database
        feedback = Feedback(
            first_name=first_name,
            last_name=last_name,
            email=email,
            time_to_contact=time_to_contact,
            first_time_donator=first_time_donator,
            where_heard_about_us=where_heard_about_us,
            inspiration_to_donate=inspiration_to_donate,
            process_easy=process_easy,
            donate_next_year=donate_next_year,
            recommend_to_others=recommend_to_others,
            improve_experience=improve_experience,
            improve_utilization=improve_utilization,
            age_range=age_range
        )
        feedback.save()

        return render(request,'thanks_feedback.html')
    return render(request, 'feedback.html')

def thanks_feedback(request):
    return render(request, 'thanks_feedback.html')