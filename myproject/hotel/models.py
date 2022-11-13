from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField

# Create your models here.

CHOICES = [(i,i) for i in range(6)]

HOTEL_FEATURE = (('Smoking areas', 'Smoking areas'),
              ('Wi-fi', 'Wi-fi'),
              ('Air conditioning', 'Air conditioning'),
              ('Spa', 'Spa'),
              ('Private beach', 'Private beach'),
              ('Parking', 'Parking'),
              ('Airport shuttle', 'Airport shuttle'),
              ('Pool', 'Pool'),
              ('Fitness centre', 'Fitness centre'),
              ('Restaurant', 'Restaurant'),
              ('Meeting facilities', 'Meeting facilities'),
              ('Bar', 'Bar'),
              ('Children pool', 'Children pool'),
              ('Children facilities', 'Children facilities'),
              ('Business centre', 'Business centre'),
              ('Laundry', 'Laundry'),)

ROOM_FEATURE = (('Electric kettle', 'Electric kettle'),
              ('Wi-fi', 'Wi-fi'),
              ('Air conditioning', 'Air conditioning'),
              ('Television', 'Television'),
              ('Telephone', 'Telephone'),
              ('Shower', 'Shower'),
              ('Coffee Maker', 'Coffee Maker'),
              ('Minibar', 'Minibar'),
              ('Balcony', 'Balcony'),)

ROOM_FOOD = (('1x breakfast','1x breakfast'),
              ('2x breakfast','2x breakfast'),
              ('1x lunch','1x lunch'),
              ('2x lunch','2x lunch'),
              ('1x dinner','1x dinner'),
              ('2x dinner','2x dinner'))

class city(models.Model):
    country_name=models.CharField(("اسماء المدن"),max_length=20)
    country_image=models.ImageField(upload_to="flight/cities", height_field=None, width_field=None)
    def __str__(self):
        return self.country_name

class hotel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    hotel_name=models.CharField((" اسم الفندق"),max_length=40)
    location=models.ForeignKey(city ,on_delete=models.CASCADE)
    address=models.CharField(("عنوان الفندق"),max_length=50)
    hotel_images=models.ImageField(upload_to="hotel/hotels", height_field=None, width_field=None, max_length=100)
    hotel_star =models.IntegerField(choices=CHOICES)
    phoneNumber = PhoneNumberField(null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here
    link_comm=models.URLField(("الموقع"), max_length=200)
    email_comm = models.EmailField(("الايميل"),max_length=254)
    facebook_comm=models.URLField(("صفحة الفيس"), max_length=200)
    whatsapp_comm= PhoneNumberField(null = True, blank = True)
    free_cancellation= models.BooleanField(default=True)
    pay_arrival= models.BooleanField(default=True)
    no_smoking= models.BooleanField(default=True)
    allowed_pets= models.BooleanField(default=True)
    include_meals= models.BooleanField(default=True)
    lowest_price=models.IntegerField(default=0)
    amemities_hotel=MultiSelectField(choices=HOTEL_FEATURE,max_length=20)
    kids=models.CharField((" سياسة الاطفال"),max_length=200)
    note=models.TextField(("ملاحظة"),max_length=200)

    def __str__(self):
        return self.hotel_name

class room(models.Model):
    room_name=models.CharField((" اسم الغرفة"),max_length=40)
    room_image=models.ImageField(upload_to="hotel/rooms", height_field=None, width_field=None, max_length=100)
    hotel_in=models.ForeignKey(hotel ,on_delete=models.CASCADE)
    price=models.IntegerField(('سعرالليلة'),default=0)
    num_guest=models.IntegerField(('عدد الافراد'),default=0)
    amemities_room=MultiSelectField(choices=ROOM_FEATURE,max_length=30)
    room_bed=models.CharField(("سراير الغرفة"),max_length=100)
    room_food=MultiSelectField(choices=ROOM_FOOD,max_length=20)
    note=models.TextField(("ملاحظة"),max_length=200)
    def __str__(self):
        return self.room_name







