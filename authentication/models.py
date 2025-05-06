from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from authentication.managers import CustomUserManager
from django.utils import timezone
import uuid
from datetime import timedelta
from django.conf import settings
# ==================== Enum Start ==================== #

ACTIVE = 'active'
INACTIVE = 'inactive'

STATUS_CHOICES = (
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
)

# ==================== Enum End ==================== #

class RoleModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField('auth.Permission', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name
    
class CountryModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name

class UserModel(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=254,unique=True)
    role = models.ForeignKey(RoleModel, on_delete=models.SET_NULL,null=True,blank=True)
    country = models.ForeignKey(CountryModel,on_delete=models.SET_NULL,null=True,blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_business = models.BooleanField(default=False)

    profile = models.ImageField(upload_to="profile/",null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField(default=None,null=True,blank=True)
    address = models.TextField(default=None,null=True,blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
    
    @property
    def reset_password_link(self):
        return f'{settings.DOMAIN}/reset_password/{self.email}/{self.id}/'
    
    # def has_permission(self, perm_codename):
    #     if self.role:
    #         return self.role.permissions.filter(codename=perm_codename).exists()
    #     return False

    # def has_module_perms(self, app_label):
    #     if self.role:
    #         return self.role.permissions.filter(content_type__app_label=app_label).exists()
    #     return False
    
class OTPModel(models.Model):
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    code = models.IntegerField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)