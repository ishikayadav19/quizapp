from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)#verbose_name
    email_address = models.CharField(max_length=55,unique=True,null=True)
    bio = models.TextField(blank=True,null=True) 
    profile_img = models.ImageField(upload_to='profile_images', default='user.png',blank=True,null=True)
    location=models.CharField(max_length=100,blank=True,null=True)
    GENDER=(
        ('male','male'),
        ('female','female'),
        ('other','other'),
    )
    gender = models.CharField(max_length=6, choices=GENDER,blank=True,null=True)