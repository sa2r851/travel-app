# Generated by Django 4.1.2 on 2022-11-11 23:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=20, verbose_name='اسماء المدن')),
                ('city_image', models.ImageField(upload_to='dayuse/cities')),
            ],
        ),
        migrations.CreateModel(
            name='dayusecompony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_name', models.CharField(max_length=40, verbose_name=' اسم الشركة')),
                ('address', models.CharField(max_length=50, verbose_name=' عنوان الشركة')),
                ('phoneNumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('secondPhoneNumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('link_comm', models.URLField(verbose_name='الموقع')),
                ('email_comm', models.EmailField(max_length=254, verbose_name='الايميل')),
                ('facebook_comm', models.URLField(verbose_name='صفحة الفيس')),
                ('whatsapp_comm', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='daytrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0, verbose_name='سعر الرحلة')),
                ('program', models.TextField(verbose_name=':برنامج الرحلة ')),
                ('address', models.CharField(max_length=200, verbose_name=' نقطة التجمع')),
                ('kids', models.CharField(max_length=200, verbose_name=' سياسة الاطفال')),
                ('ourdata', models.DateField(default=datetime.date.today, verbose_name='معاد الرحلة')),
                ('trip_images', models.ImageField(upload_to='dayuse/trips')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='day_use.dayusecompony')),
                ('destination', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='to_where', to='day_use.city')),
                ('fromwhere', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='from_where', to='day_use.city')),
            ],
        ),
    ]