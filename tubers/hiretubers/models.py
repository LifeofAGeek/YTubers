from django.db import models
from datetime import datetime
# Create your models here.

class Hiretuber(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    tuber_id = models.IntegerField(blank=True)
    tuber_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True,default=datetime.now)

    def __str__(self):
        return self.email
    
