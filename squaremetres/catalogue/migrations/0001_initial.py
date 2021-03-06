# Generated by Django 2.1.4 on 2018-12-28 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(default=0)),
                ('bedrooms', models.IntegerField(default=0)),
                ('bathrooms', models.IntegerField(default=0)),
                ('garage', models.IntegerField(default=0)),
                ('area', models.IntegerField()),
                ('photo_main', models.ImageField(default='/media/defaults/default_property.jpeg', upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(default='/media/defaults/default_property.jpeg', upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(default='/media/defaults/default_property.jpeg', upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(default='/media/defaults/default_property.jpeg', upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(default='/media/defaults/default_property.jpeg', upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(default='/media/defaults/default_property.jpeg', upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(default='/media/defaults/default_property.jpeg', upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('catalogue_date', models.DateTimeField(blank=True, default=datetime.date.today)),
            ],
        ),
    ]
