from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime

# Create your models here.
class umrahcompony(models.Model):
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
class umrah(models.Model):
    company=models.ForeignKey(umrahcompony,related_name='umrah',on_delete=models.CASCADE)
    price=models.IntegerField(('سعر الرحلة'),default=0)
    program=models.TextField((":برنامج الرحلة "))
    durtion=models.IntegerField(('عدد الايام'),default=0)
    ourdata=models.DateField(("معاد الرحلة"),default=datetime.date.today)
    def __str__(self):
        return self.ourdata
class hegg(models.Model):
    company=models.ForeignKey(umrahcompony,related_name='hegg',on_delete=models.CASCADE)
    price=models.IntegerField(('سعر الرحلة'),default=0)
    program=models.TextField((":برنامج الرحلة "))
    durtion=models.IntegerField(('عدد الايام'),default=0)
    ourdata=models.DateField(("معاد الرحلة"),default=datetime.date.today)
    def __str__(self):
        return self.price