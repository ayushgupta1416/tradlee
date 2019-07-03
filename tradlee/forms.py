from django import forms
from tradlee.models import Signup, Login, Feedback, Product , add_prod_for_rent , add_prod_for_sell


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


class rentForm(forms.ModelForm):
    class Meta:
        model = add_prod_for_rent

class sellForm(forms.ModelForm)
    class Meta:
        model = add_prod_for_sell