from django import forms
from tradlee.models import Signup, Login, Feedback, Product


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Signup
        fields = (
        'name', 'email', 'password', 'house_no', 'address_line1', 'address_line2', 'telephone', 'zip_code', 'state',
        'country','city')


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('email', 'password')


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback


class Product(forms.ModelForm):
    class Meta:
        model = Product
