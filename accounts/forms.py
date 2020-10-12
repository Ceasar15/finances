from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.forms import fields
from .models import Profile


class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Username', min_length=4, max_length=150)
    first_name = forms.CharField(label='First Name', min_length=3, max_length=50)
    last_name = forms.CharField(label='Last Name', min_length=2, max_length=50)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        result = User.objects.filter(username=username)
        if result.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        results = User.objects.filter(email=email)
        if results.count():
            raise ValidationError("Email already exists")
        return email

    def save(self, commit=True, *args, **kwargs):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password1'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
        )
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'profile_pic',
            'phone',
        )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        return phone

    def clean_avatar(self):
        profile_pic = self.cleaned_data['profile_pic']

        try:
            w, h = get_image_dimensions(profile_pic)

            max_width = max_height= 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(u'Please use an image that is %s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = profile_pic.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'GIF or PNG image.')

            #validate file size
            if len(profile_pic) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new profile_pic
            """
            pass

        return profile_pic                 