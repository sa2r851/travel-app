from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime

class flightcompony(models.Model):
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

class city(models.Model):
    country_name=models.CharField(("اسماء المدن"),max_length=20)
    country_image=models.ImageField(upload_to="flight/cities", height_field=None, width_field=None)
    def __str__(self):
        return self.country_name

class travel(models.Model):
    company=models.ForeignKey(flightcompony ,on_delete=models.CASCADE)
    price=models.IntegerField(('سعر التذكرة'),default=0)
    destination=models.ForeignKey(city,related_name='to_where',on_delete=models.CASCADE,default=None)
    ourdata=models.DateField(("معاد الرحلة"),default=datetime.date.today)
    fromwhere=models.ForeignKey(city,related_name='from_where',on_delete=models.CASCADE,default=None)
    lunchtime=models.TimeField(("وقت الاقلاع"),blank=True,null=True)
    def __str__(self):
        return f"{self.destination} {self.ourdata}"

