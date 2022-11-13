from email.policy import default
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.
class city(models.Model):
    city_name=models.CharField(("اسماء المدن"),max_length=20)
    city_image=models.ImageField(upload_to="wedding/cities", height_field=None, width_field=None)
    def __str__(self):
        return self.city_name

class town(models.Model):
    town_name=models.CharField(("اسماء المناطق"),max_length=20)
    city_in=models.ForeignKey(city ,on_delete=models.CASCADE)
    def __str__(self):
        return self.town_name


class hall(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    hall_name=models.CharField((" اسم القاعة"),max_length=40)
    the_city=models.ForeignKey(city,on_delete=models.CASCADE,default=None)
    the_town=models.ForeignKey(town ,on_delete=models.CASCADE)
    address=models.CharField((" عنوان القاعة"),max_length=50)
    image=models.ImageField(blank=True)
    price=models.IntegerField(('سعر القاعة'),default=0)
    number_people=models.IntegerField(('عدد الافراد '),default=0)
    price_list=models.TextField(("اسعار الاضافات"),max_length=250)
    program=models.TextField((":برنامج الفرح "),max_length=250)
    phoneNumber = PhoneNumberField(null = False, blank = False) # Here
    secondPhoneNumber = PhoneNumberField(null = True, blank = True) # Here
    link_hall=models.URLField(("الموقع"), max_length=200)
    email_hall = models.EmailField(("الايميل"),max_length=254)
    facebook_hall=models.URLField(("صفحة الفيس"), max_length=200)
    whatsapp_hall= PhoneNumberField(null = True, blank = True) # Here
    def __str__(self):
        return f"{self.hall_name} {self.address}"


class hallimage(models.Model):
    hall=models.ForeignKey(hall,on_delete=models.CASCADE,default=None)
    image=models.FileField(upload_to="wedding/halls")
    def __str__(self):
        return f"{self.hall.hall_name} {self.hall.address}"




