from django import forms # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")
    first_name = forms.CharField(max_length=30, required=True, help_text="Enter your first name.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Enter your last name.")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'User Name',
            'email': 'Email Address',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add placeholders and classes to form fields
        field_names = {
            'username': 'Enter username',
            'first_name': 'Enter first name',
            'last_name': 'Enter last name',
            'email': 'Enter email',
            'password1': 'Enter password',
            'password2': 'Confirm password'
        }
        
        for field_name, placeholder in field_names.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': placeholder
                })

    def clean_email(self):
        """Custom email validation to ensure email uniqueness."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email address already exists.")
        return email

    def clean_password1(self):
        """Custom password validation for stronger passwords."""
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password1):
            raise forms.ValidationError("Password must include at least one number.")
        if not any(char.isalpha() for char in password1):
            raise forms.ValidationError("Password must include at least one letter.")
        return password1
