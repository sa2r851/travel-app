from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime

class tripoutcompony(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    com_name=models.CharField((" اسم الشركة"),max_length=40)
    address=models.CharField((" عنوان الشركة"),max_length=50)
    phoneNumber = PhoneNumberField(null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here
    link_comm=models.URLField(("الموقع"), max_length=200)
    email_comm = models.EmailField(("الايميل"),max_length=254)
    facebook_comm=models.URLField(("صفحة الفيس"), max_length=200)
    whatsapp_comm= PhoneNumberField(null = True, blank = True) # Here
    def __str__(self):
        return self.com_name

class country(models.Model):
    country_name=models.CharField(("اسماء الدول"),max_length=20)
    country_image=models.ImageField(upload_to="tripout/cities", height_field=None, width_field=None)
    def __str__(self):
        return self.country_name
class travel(models.Model):
    company=models.ForeignKey(tripoutcompony ,on_delete=models.CASCADE)
    price=models.IntegerField(('سعر الرحلة'),default=0)
    durtion=models.IntegerField(('عدد الايام'),default=0)
    program=models.TextField((":برنامج الرحلة "))
    destination=models.ForeignKey(country,related_name='to_where',on_delete=models.CASCADE,default=None)
    kids=models.CharField((" سياسة الاطفال"),max_length=200)
    ourdata=models.DateField(("معاد الرحلة"),default=datetime.date.today)
    trip_images=models.ImageField(upload_to="tripout/trips", height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return f"{self.destination} {self.ourdata}"