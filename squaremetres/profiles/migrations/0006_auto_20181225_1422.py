# Generated by Django 2.1.4 on 2018-12-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20181221_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/static/images/defaults/default_pic.png', null=True, upload_to='user_pic/'),
        ),
    ]