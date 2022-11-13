from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

APARTMENT_TYPE = (('شقة','شقة'),
              ('شالية','شالية'),
              ('فيلا','فيلا'),
              ('بنتهاوس','بنتهاوس'),
              ('دوبلكس','دوبلكس'),
              ('تاون هاوس','تاون هاوس'),
              ('شقق فندقية','شقق فندقية'),
              ('ستوديو','ستوديو'))

APARTMENT_FEATURE = (('واي فاي','واي فاي'),
              ('تكيف','تكيف'),
              ('خدمة التنظيف','خدمة التنظيف'),
              ('حراسة امن','حراسة امن'),
              ('غرفة خادمة','عرفة خادمة'),
              ('مسموح بتربية الحيوانات','مسموح بتربية الحيوانات'),
              ('منطقة شواء','منطقة شواء'),
              ('موقف سيارات','موقف سيارت'),
              ('اسانسير','اسانسير'),
              ('شاطي خاص','شاطي خاص'),
              ('بلكونة','بلكونة'),
              ('مسبح خاص','مسبح خاص'),
              ('حديفة خاصة','حديقة خاصة'),
              ('مطلة علي البحيرات','مطلة علي البحيرات'),
              ('مطلة علي البحر','مطلة علي البحر'))
class city(models.Model):
    city_name=models.CharField(("اسماء المدن"),max_length=20)
    city_image=models.ImageField(upload_to="apartment/cities", height_field=None, width_field=None)
    def __str__(self):
        return self.city_name

class town(models.Model):
    town_name=models.CharField(("اسماء المناطق"),max_length=20)
    city_in=models.ForeignKey(city ,on_delete=models.CASCADE)
    def __str__(self):
        return self.town_name

class apart(models.Model):
    title=models.CharField(("عنوان "),max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    apart_images=models.ImageField(upload_to="apartment/aparts", height_field=None, width_field=None)
    amemities_apart=MultiSelectField(choices=APARTMENT_FEATURE,max_length=100)
    type_apart=MultiSelectField(choices=APARTMENT_TYPE,max_length=20)
    the_city=models.ForeignKey(city ,on_delete=models.CASCADE)
    the_town=models.ForeignKey(town ,on_delete=models.CASCADE)
    address=models.CharField(("عنوان الشقة"),max_length=50)
    price_night=models.IntegerField(('سعر الليلة'),default=0)
    price_month=models.IntegerField(('سعر الشهري'),default=0)
    rooms=models.IntegerField(('عدد الغرف'),default=1)
    bathroom=models.IntegerField(('عدد الحمامات'),default=1)
    meter=models.IntegerField((' المساحة'),default=1)
    bed=models.IntegerField((' عدد السراير'),default=1)
    furniture= models.BooleanField(default=True)
    PhoneNumber = PhoneNumberField(null = True, blank = True) # Here
    whatsapp = PhoneNumberField(null = True, blank = True) # Here
    e_mail = models.EmailField(max_length=254,)
    note=models.TextField(('ملاحظات'))

    def __str__(self):
        return f"{self.the_town} {self.price}"
class Images(models.Model):
    apart=models.ForeignKey(apart,null=False,default=1,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="apartment/aparts", height_field=None, width_field=None)


#https://wa.me/whatsappphonenumber/?text=urlencodedtext#