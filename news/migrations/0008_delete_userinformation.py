# Generated by Django 3.1.5 on 2021-07-02 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_userinformation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserInformation',
        ),
    ]