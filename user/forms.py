import datetime

from creditcards.forms import CardNumberField
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from  cinema.models import Movies
from .constants import GenderChoices, LANGUAGE_CHOICES, CITY_CHOICES
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=50, label="Email address",
                             help_text='user@gmail.com',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Write email address'}))
    first_name = forms.CharField(required=True, max_length=50, label="First Name",
                                 help_text='John',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your first name here'}))
    last_name = forms.CharField(required=True, max_length=50, label="Last Name", help_text='Smit',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your last name here'}))
    password1 = forms.CharField(required=True, label="Password", help_text='Write password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Write password here'}))
    password2 = forms.CharField(required=True, label="Repeat password", help_text='Password again',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Write password again'}))
    gender = forms.ChoiceField(required=False, label='Gender', choices=GenderChoices.choices,
                               initial=GenderChoices.MALE,
                               widget=forms.RadioSelect(attrs={'class': 'icheck-success d-inline', 'placeholder': 'Check your gender'}))
    birthday = forms.DateField(label='Date of Birthday', initial=datetime.date.today,
                               help_text='Date Birthday',
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select your date Birthday'}))
    language = forms.ChoiceField(label='Language', choices=LANGUAGE_CHOICES, initial='en',
                                 help_text='Language',
                                 widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select your language'}))
    phone = PhoneNumberField(required=False, label='Phone Number', help_text='+380 000 000 000',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your phone here'}))
    city = forms.ChoiceField(label='City', choices=CITY_CHOICES, initial='washington',
                             help_text='City',
                             widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select your city'}))
    address = forms.CharField(required=False, label="Address", help_text='Address',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your address here'}))
    number_card = CardNumberField(required=False, label='Card Number', help_text='Number card',
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your card number here'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'gender', 'birthday',
                  'language', 'phone', 'city', 'address', 'number_card')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password1']
        user.set_password(password)

        if commit:
            user.save()


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, label='Email address', help_text='Input your Email address',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Write email address'}))
    password = forms.CharField(required=True, label='Password', help_text='Input your password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Write password'}))


class CustomUserChangeForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=50, label="Email address",
                             help_text='Email address',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Write email address'}))
    first_name = forms.CharField(required=True, max_length=50, label="First Name",
                                 help_text='First name',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your first name here'}))
    last_name = forms.CharField(required=True, max_length=50, label="Last Name", help_text='last name',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your last name here'}))
    gender = forms.ChoiceField(required=False, label='Gender', choices=GenderChoices.choices, help_text='Gender',
                               initial=GenderChoices.MALE,
                               widget=forms.RadioSelect(attrs={'class': 'form-check-inline', 'placeholder': 'Check your gender'}))
    birthday = forms.DateField(required=False, label='Date of Birthday', initial=datetime.date.today,
                               help_text='Date Birthday',
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Select your date Birthday'}))
    language = forms.ChoiceField(label='Language', choices=LANGUAGE_CHOICES, initial='en',
                                 help_text='Language',
                                 widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select your language'}))
    phone = PhoneNumberField(required=False, label='Phone Number', help_text='+380 000 000 000',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.ChoiceField(label='City', choices=CITY_CHOICES, initial='washington',
                             help_text='City',
                             widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Write your phone here'}))
    address = forms.CharField(required=False, label="Address", help_text='Address',
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your address here'}))
    number_card = CardNumberField(required=False, label='Card Number', help_text='Number card',
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your card number here'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'gender', 'birthday',
                  'language', 'phone', 'city', 'address', 'number_card')


class EditFilmPageForm(forms.ModelForm):
    name_movie = forms.CharField(required=True, max_length=50, label="Film Name",
                                 widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Write name film here'}))
    description_movie = forms.CharField(required=False,
                                        widget=forms.Textarea(attrs={'class': 'form-control', 'row': '3',
                                                                     'placeholder': 'Write description here'}))

    class Meta:
        model = Movies
        fields = ['name_movie', 'description_movie']
