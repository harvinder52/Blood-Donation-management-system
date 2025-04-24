from django.shortcuts import render,redirect
import random
from django.http import HttpResponse
from .models import Contact
from .models import Feedback
from .models import Donor
from .models import BloodRequest
from .models import loginform
from .models import registerform
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from .forms import DonorForm, EmailForm, OTPForm
from .models import EmailOTP, User
from django.utils import timezone


from .models import BloodRequest, Donor



from django.shortcuts import render, redirect, get_object_or_404

# Approve a blood request
def approve_request(request, request_id):
    blood_request = get_object_or_404(BloodRequest, id=request_id)
    blood_request.status = 'Approved'  # Update status to 'Approved'
    blood_request.save()  # Save the changes
    return redirect('admin_dashboard')  # Redirect to the admin dashboard

# Delete a blood request
def delete_request(request, request_id):
    blood_request = get_object_or_404(BloodRequest, id=request_id)
    blood_request.delete()  # Delete the request from the database
    return redirect('admin_dashboard')  # Redirect to the admin dashboard

def delete_donor(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    donor.delete()  # Delete the donor from the database
    return redirect('admin_dashboard')

@login_required(login_url='admin_login')
def admin_dashboard(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('admin_login')
    blood_requests = BloodRequest.objects.all()
    donors = Donor.objects.all()  # Query all donors
    return render(request, 'admin_dashboard.html', {'blood_requests': blood_requests, 'donors': donors})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def admin_login(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Log out user session if logged in
        if 'logged_in_user' in request.session:
            del request.session['logged_in_user']

        user = authenticate(request, username=username, password=password)
        if user is not None and (user.is_staff or user.is_superuser):
            auth_login(request, user)
            return redirect('admin_dashboard')
        else:
            error = "Invalid username or password."

    return render(request, 'admin_login.html', {'error': error})



def admin_logout(request):
    auth_logout(request)
    return redirect('/')


def user_dashboard(request):
    if 'logged_in_user' not in request.session:
        return redirect('send_otp')  # or a login page if you have one
    return render(request, 'user_dashboard.html')


def send_otp(request):
    if request.user.is_authenticated:
        auth_logout(request)  # Ensure admin is logged out if trying user login

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = str(random.randint(100000, 999999))

            EmailOTP.objects.create(email=email, otp=otp)

            send_mail(
                'Your OTP Code',
                f'Use this OTP to verify your email: {otp}',
                'youremail@example.com',
                [email],
                fail_silently=False,
            )
            request.session['user_email'] = email
            return redirect('verify_otp')
    else:
        form = EmailForm()
    return render(request, 'send_otp.html', {'form': form})

def verify_otp(request):
    email = request.session.get('user_email')
    if not email:
        return redirect('send_otp')

    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            otp_input = form.cleaned_data['otp']
            otp_record = EmailOTP.objects.filter(email=email, otp=otp_input).last()
            if otp_record:
                otp_record.is_verified = True
                otp_record.save()

                # Log out admin if logged in
                if request.user.is_authenticated:
                    auth_logout(request)

                user, created = User.objects.get_or_create(email=email)
                request.session['logged_in_user'] = user.email
                return redirect('user_dashboard')
            else:
                form.add_error('otp', 'Invalid OTP')
    else:
        form = OTPForm()
    return render(request, 'verify_otp.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        auth_logout(request)

    if 'logged_in_user' in request.session:
        del request.session['logged_in_user']

    return redirect('/')

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
    context = {}
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
        
        context["show_modal"] = True  # Save the donor data to the database
             # Redirect to a success page after successful registration
    else:
        form = DonorForm()

    return render(request, 'registerasdonor.html', {'form': form, 'show_modal': context.get("show_modal", False)})


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