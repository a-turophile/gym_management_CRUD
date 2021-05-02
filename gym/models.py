# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class gym(models.Model):
    name = models.CharField(max_length=200, null = True)
    email = models.EmailField(max_length=254, null = True, unique=True)
    address = models.TextField(null=True)
    aadhar = models.ImageField(upload_to='upload/', default='images/image.jpeg')
    gender = models.CharField(max_length=20)

    #CHECKBOX FIELDS
    aerobics = models.BooleanField('Aerobics', default=False)
    yoga = models.BooleanField('Yoga', default=False)
    weight_training = models.BooleanField('Weight Training', default=False)
    cardio = models.BooleanField('Cardio', default=False)

    #DROP-DOWN FIELD
    timing = (
        ('morning',"Morning"),
        ('evening',"Evening"),
        ('night', "Night")
    )
    timing = models.CharField(max_length=20,choices = timing, default='Morning')

    weight = models.FloatField()

    dor = models.DateTimeField(auto_now=True) #DATE OF REGISTRATION

    class Meta:
        db_table = 'Members'
        ordering = ['-dor']






