from django.db import models

# Create your models here.

class team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    youtube_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.first_name

class Slider(models.Model):
    headline=models.CharField(max_length=255)
    subtitle=models.CharField(max_length=255)
    button_text=models.CharField(max_length=255)
    photo=models.ImageField(upload_to='media/slider/%Y/')
    created_date=models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.headline
    