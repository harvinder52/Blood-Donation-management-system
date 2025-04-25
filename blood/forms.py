from django import forms
from .models import Feedback
from .models import Donor

class EmailForm(forms.Form):
    email = forms.EmailField(label='Enter your email')

class OTPForm(forms.Form):
    otp = forms.CharField(label='Enter OTP', max_length=6)


from django import forms
from .models import Donor

class DonorForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    
    # Explicitly define gender as RadioSelect
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        required=True
    )

    class Meta:
        model = Donor
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'gender':  # Skip gender as we already configured it
                field.widget.attrs['class'] = 'form-control'
                if not isinstance(field.widget, (forms.Textarea, forms.Select, forms.RadioSelect)):
                    field.widget.attrs['placeholder'] = ' '
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message', 'rating']