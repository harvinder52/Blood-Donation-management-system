from django.shortcuts import render,redirect
import random
from django.http import HttpResponse, JsonResponse

import settings
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
from .forms import DonorForm, EmailForm, FeedbackForm, OTPForm
from .models import EmailOTP, User
from django.utils import timezone
from .models import BloodRequest, Donor, Feedback, Contact


from .models import BloodRequest, Donor



from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Donor, BloodRequest

def approve_donor_for_request(request, donor_id, request_id):
    donor = get_object_or_404(Donor, id=donor_id)
    blood_request = get_object_or_404(BloodRequest, id=request_id)

    # Compose email content
    subject = 'Blood Donation Request Notification'
    message = f'''
Dear {donor.first_name} {donor.last_name},

You have been identified as a matching donor for a blood request.

Requester Name: {blood_request.full_name}
Blood Group: {blood_request.blood_group}
City: {blood_request.city}
Contact: {blood_request.contact_number}
Address: {blood_request.address}

If you're willing to donate, please get in touch with the requester as soon as possible.

Thank you for being a life-saver!
- Blood Donation Team
'''
    recipient_email = donor.email

    # Send email (Make sure EMAIL settings are properly configured in settings.py)
    try:
       send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,  # Use from settings
            recipient_list=[recipient_email],
            fail_silently=False
        )
       messages.success(request, f'Notification email sent to {donor.first_name} {donor.last_name}.')
    except Exception as e:
        messages.error(request, f'Failed to send email: {str(e)}')

    return redirect('admin_dashboard')  # Replace with your dashboard view name


def approve_request(request, request_id):
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('admin_login')
    
    blood_request = get_object_or_404(BloodRequest, id=request_id)
    blood_request.status = 'Approved'
    blood_request.save()
    
    # Normalize blood group
    requested_blood_group = blood_request.blood_group.replace('−', '-').strip().upper()
    
    # Match donors ONLY by blood group
    matched_donors = Donor.objects.filter(
        blood_group__iexact=requested_blood_group
    )

    matched_donors_data = [
        {
            'id': donor.id,
            'name': f"{donor.first_name} {donor.last_name}",
            'blood_group': donor.blood_group,
            'city': donor.city,
            'email': donor.email,
            'contact_number': donor.contact_number
        }
        for donor in matched_donors
    ]
    
    return JsonResponse({
        'status': 'success',
        'matched_donors': matched_donors_data,
        'debug': {
            'requested_blood_group': blood_request.blood_group,
            'normalized_blood_group': requested_blood_group,
            'match_count': len(matched_donors_data)
        }
    })

def show_matched_donors(request, request_id):
    # Get the blood request
    blood_request = get_object_or_404(BloodRequest, id=request_id)

    # Find all donors with the same blood group
    matched_donors = Donor.objects.filter(blood_group=blood_request.blood_group)

    return render(request, 'admin_dashboard.html', {
        'blood_request': blood_request,
        'matched_donors': matched_donors
    })
# Delete a blood request
def delete_request(request, request_id):
    blood_request = get_object_or_404(BloodRequest, id=request_id)
    blood_request.delete()  # Delete the request from the database
    return redirect('admin_dashboard')  # Redirect to the admin dashboard

def delete_donor(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    donor.delete()  # Delete the donor from the database
    return redirect('admin_dashboard')
def delete_feedback(request, id):
    feedback = get_object_or_404(Feedback, id=id)
    feedback.delete()
    return redirect('admin_dashboard')  # Redirecting back to the Admin Dashboard

# View for deleting a contact us entry
def delete_contact_us(request, id):
    contact = get_object_or_404(Contact, id=id)
    contact.delete()
    return redirect('admin_dashboard')
@login_required(login_url='admin_login')
def admin_dashboard(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('admin_login')
    blood_requests = BloodRequest.objects.all()
    donors = Donor.objects.all()  # Query all donors
    feedbacks = Feedback.objects.all()  # Fetching all feedback
    contact_us_entries = Contact.objects.all() 
    return render(request, 'admin_dashboard.html', {
        'blood_requests': blood_requests,
        'donors': donors,
        'feedbacks': feedbacks,
        'contact_us_entries': contact_us_entries,
    })

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

def motive(request):
    return render(request, 'motive.html')

def index(request):
    return render(request, 'index.html')
def request_for_blood(request):
    context = {}
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
        context["show_modal"] = True 
        
    return render(request, 'requestforblood.html', { 'show_modal': context.get("show_modal", False)})

def success(request):
    return render(request, 'success.html')
def see_all_request(request):
    blood_requests = BloodRequest.objects.all()
    return render(request, 'seeallrequest.html', {'blood_requests': blood_requests})





def register_as_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect with success parameter
            return redirect('register_as_donor_success')
    else:
        form = DonorForm()
    
    return render(request, 'registerasdonor.html', {'form': form})

def register_as_donor_success(request):
    # This view just shows the form again with modal trigger
    return render(request, 'registerasdonor.html', {
        'form': DonorForm(),
        'show_modal': True
    })
    
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        blood_need = request.POST.get('blood_need')  
        contact = Contact(name=name, email=email, phone=phone, blood_need=blood_need)
        contact.save()
        return render(request, 'thanks.html')
    return render(request, 'contact.html')

def thanks(request):
    return render(request, 'thanks.html')



def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks_feedback')  # Redirect to a thank you page or feedback listing page.
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})

def thank_you(request):
    return render(request, 'thans_feedback.html')






def thanks_feedback(request):
    return render(request, 'thanks_feedback.html')



def contact_list(request):
    contacts = Contact.objects.all().order_by('-submitted_at')
    return render(request, 'contact_list.html', {'contacts': contacts})