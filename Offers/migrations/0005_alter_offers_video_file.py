# Generated by Django 4.1 on 2022-09-08 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Offers', '0004_slides'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='Offers_files'),
        ),
    ]
