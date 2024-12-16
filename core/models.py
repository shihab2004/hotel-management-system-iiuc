from django.conf import settings
from django.db import models
from django.db.models import Min









class contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name


    

class Hotel(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

    @property
    def get_price(self):
        price = self.rooms.all().aggregate(Min("price"))['price__min']
        return price if price else 0.00

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,related_name="rooms")
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    
    
    def __str__(self):
        return self.title



class Booking(models.Model):
    
    booking_status = (
        ("Pending","Pending"),
        ("Booked","Booked"),
        ("Cancelled","Cancelled"),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    total_price = models.FloatField()
    paid_amount = models.FloatField(default=0.0)
    adult = models.PositiveIntegerField(default=0)
    child = models.PositiveIntegerField(default=0)
    checkin = models.DateField()
    checkout = models.DateField()
    
    user_full_name = models.CharField(max_length=255)
    user_phone = models.CharField(max_length=255,)
    user_email = models.EmailField(null=True, blank=True)
    user_address = models.CharField(max_length=255)
    
    status = models.CharField(choices=booking_status,max_length=50,default="Pending")
    


    def __str__(self):
        return  f"{self.hotel.title} - {self.user.username}"

    # def get_total(self):
    #     total = 0
    #     for order_item in self.items.all():
    #         total += order_item.get_final_price()
    #     if self.coupon:
    #         total -= self.coupon.amount
    #     return total





