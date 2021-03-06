# Generated by Django 2.1.4 on 2018-12-28 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=200)),
                ('property_id', models.IntegerField()),
                ('user', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('enquiry_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('buyer_id', models.IntegerField(blank=True)),
                ('dealer_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
