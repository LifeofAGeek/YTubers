from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Youtuber(models.Model):

    crew_choices = (
        ('solo','solo'),
        ('small','small'),
        ('large','large'),
    )

    camera_choices = (
        ('sony','sony'),
        ('canon','canon'),
        ('red','red'),
        ('fuji','fuji'),
        ('nikon','nikon'),
        ('panasonic','panasonic'),
        ('other','other'),
    )

    category_choices = (
        ('programming','programming'),
        ('gadgets','gadgets'),
        ('comedy','comedy'),
        ('film_making','film_making'),
        ('cooking','cooking'),
        ('gaming','gaming'),
        ('other','other'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="media/ytubers/%Y/%m/")
    video_url = models.CharField(max_length=255)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    hieght = models.IntegerField()
    crew = models.CharField(choices=crew_choices ,max_length=255)
    camera_type = models.CharField(choices=camera_choices ,max_length=255)
    subs_count = models.IntegerField()
    category = models.CharField(choices=category_choices, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateField(default=datetime.now, blank=True)


