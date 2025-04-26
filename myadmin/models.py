from django.db import models

# Create your models here.

class BusinessTypeModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='business_types/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name