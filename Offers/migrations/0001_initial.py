# Generated by Django 4.1 on 2022-08-12 14:38

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rishTextEditor', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('title', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('video_file', models.FileField(upload_to='Offers_files')),
            ],
        ),
    ]
