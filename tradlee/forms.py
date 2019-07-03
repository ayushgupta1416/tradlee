from django import forms
from tradlee.models import Signup, Login, add_prod_for_rent, add_prod_for_sell , SellFeedback , RentFeedback


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


class rentForm(forms.ModelForm):
    class Meta:
        model = add_prod_for_rent
        fields = ('prod_name', 'category', 'short_description', 'rent_price', 'prod_age')


class sellForm(forms.ModelForm):
    class Meta:
        model = add_prod_for_sell
        fields = ('prod_name', 'category', 'short_description', 'sell_price')


class sellFeedbackForm(forms.ModelForm):
    class Meta:
        model = SellFeedback
        fields = ('customer_name', 'email', 'product', 'message')


class rentFeedbackForm(forms.ModelForm):
    class Meta:
        model = RentFeedback
        fields = ('customer_name' , 'email' , 'product' , 'message')
