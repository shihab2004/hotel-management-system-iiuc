
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.http import Http404
from .forms import CheckoutForm
from .models import *
import pandas as pd
from django.http import HttpResponse



from django.core.paginator import Paginator
from django.views.generic.list import ListView

class HotelView(ListView):
    model = Hotel
    paginate_by = 10  
    template_name = "hotel_list.html"
    

    




def hotel_detail(request,pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    return render(request, 'hotel_detail.html', {'hotel': hotel})


@login_required(login_url="/auth/login")
def checkout(request,pk,pk2):
    
    room = get_object_or_404(Room, hotel=pk,pk=pk2)
    return render(request, 'checkout.html', {'room': room,})
    


@login_required(login_url="/auth/login")
def booking(request):
    room = get_object_or_404(Room, pk=request.POST.get('room'))
    
    if request.method == 'POST':
        print(request.POST)
        
        
        form = CheckoutForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            days = (form.cleaned_data.get('checkout') - form.cleaned_data.get('checkin')).days
            instance = form.save(commit=False)
            instance.total_price = days * room.price
            instance.user = request.user
            instance.save()
            
            messages.add_message(request, messages.SUCCESS, f"Hotel Booked Successfully. Booking ID #{instance.pk}.")

            return redirect('/hotels/')
        
        return render(request, 'checkout.html', {'room': room, 'form':form})
    raise Http404
    
    



def tracking(request):
    
        booking = None
        if request.method == 'POST':
            
            try:
                booking =  Booking.objects.get(pk=request.POST.get('booking_id'))
                messages.add_message(request, messages.SUCCESS,"Booking found successfully.")
            except Booking.DoesNotExist:
                messages.add_message(request, messages.WARNING,"No Booking found.")
        
        
        
        return render(request, 'tracking.html', {'booking': booking})
        

def home(request):
    return render(request, 'index.html')



def booking_report(request):
    queryset = Booking.objects.all()
    df = pd.DataFrame(list(queryset.values())) 
    csv_data = df.to_csv(index=False)  
    response = HttpResponse(csv_data, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'
    
    return response