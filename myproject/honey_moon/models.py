from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime

# Create your models here.
class honeymooncompony(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    com_name=models.CharField((" اسم الشركة"),max_length=40)
    address=models.CharField((" عنوان الشركة"),max_length=50)
    phoneNumber = PhoneNumberField(null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True,default="+201225584562") # Here
    link_comm=models.URLField(("الموقع"), max_length=200,default='https://www.linkedin.com/in/mohamed-sakr-955205195/')
    email_comm = models.EmailField(("الايميل"),max_length=254,default="msakr2155@gmail.com")
    facebook_comm=models.URLField(("صفحة الفيس"), max_length=200,default='https://www.linkedin.com/in/mohamed-sakr-955205195/')
    whatsapp_comm= PhoneNumberField(null = True, blank = True,default="+201225584562") # Here
    def __str__(self):
        return self.com_name
    
class city(models.Model):
    city_name=models.CharField(("اسماء المدن"),max_length=20)
    city_image=models.ImageField(upload_to="honey/cities", height_field=None, width_field=None)
    def __str__(self):
        return self.city_name
        
class moon(models.Model):
    company=models.ForeignKey(honeymooncompony,on_delete=models.CASCADE)
    price=models.IntegerField(('سعر الرحلة'),default=0)
    program=models.TextField((":برنامج الرحلة "))
    durtion=models.IntegerField(('عدد الايام'),default=0)
    destination=models.ForeignKey(city,related_name='to_where',on_delete=models.CASCADE,default=None)
    ourdata=models.DateField(("معاد الرحلة"),default=datetime.date.today)
    trip_images=models.ImageField(upload_to="honey/trips", height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return f"{self.destination} {self.ourdata}"
