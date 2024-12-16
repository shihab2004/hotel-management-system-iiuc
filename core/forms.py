from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from core.models import Booking



class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user','total_price','status','paid_amount']
