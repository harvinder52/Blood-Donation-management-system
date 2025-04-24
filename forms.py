from django import forms
from .models import Donor

class EmailForm(forms.Form):
    email = forms.EmailField(label='Enter your email')

class OTPForm(forms.Form):
    otp = forms.CharField(label='Enter OTP', max_length=6)


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['first_name', 'last_name', 'email', 'contact_number', 'state', 'city', 'address', 'gender', 'blood_group', 'date_of_birth']
