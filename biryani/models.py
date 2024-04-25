from django.db import models


# Create your models here.
class BiryaniDB(models.Model):
    AKHILA_LIKES = [
        ('YES', True), 
        ('NO', False)
    ]
    biryani_name = models.CharField(primary_key=True, max_length=30)
    origin_place = models.CharField(max_length=15)
    favourite_percentage = models.IntegerField()
    does_akhila_like = models.BooleanField(max_length=3, choices=AKHILA_LIKES)
