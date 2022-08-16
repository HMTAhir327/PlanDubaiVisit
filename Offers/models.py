from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Offers(models.Model):
    video_file = models.FileField(upload_to='Offers_files',null=False, blank=False)
    title = models.CharField(max_length=300, null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2,null=False, blank=False)
    rishTextEditor = RichTextUploadingField(blank=True, null=True)
    isOffer = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    