# Generated by Django 3.2.5 on 2021-07-13 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='profile_image',
            field=models.ImageField(blank=True, default='profile_images/default_avatar.png', null=True, upload_to='profile_images/'),
        ),
    ]
