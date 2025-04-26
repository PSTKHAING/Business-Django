from django.contrib import admin
from authentication import models
# Register your models here.

admin.site.register(models.UserModel)
admin.site.register(models.CountryModel)
admin.site.register(models.RoleModel)