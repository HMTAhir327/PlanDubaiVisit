# Generated by Django 4.1 on 2022-08-14 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Offers', '0002_offers_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='offers',
            name='isOffer',
            field=models.BooleanField(default=False),
        ),
    ]
