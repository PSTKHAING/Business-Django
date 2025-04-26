from django.db import models
from authentication.models import *
from myadmin.models import *
# Create your models here.

class PostModel(models.Model):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='posts')
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reaction = models.ManyToManyField(UserModel, related_name='post_reaction', blank=True)

    def __str__(self):
        return f'Post by {self.author.username}'

class PostMediaModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='post_media/')
    file_type = models.CharField(
        max_length=10,
        choices=[('image', 'Image'), ('video', 'Video')]
    )
    created_at = models.DateTimeField(auto_now_add=True,null=True)

class BusinessModel(models.Model):
    type = models.ForeignKey(BusinessTypeModel,on_delete=models.SET_NULL,null=True)
    owner = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True,blank=True)
    bio = models.TextField(null=True, blank=True)
    profile = models.ImageField(upload_to='business_profiles/', null=True, blank=True)
    background_profile = models.ImageField(upload_to='business_backgrounds/', null=True, blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=200, null=True,blank=True)
    address = models.TextField(null=True, blank=True)
    country = models.ForeignKey(CountryModel,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)