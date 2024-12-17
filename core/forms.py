from django import forms
from core.models import Booking



class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user','total_price','status','paid_amount']
