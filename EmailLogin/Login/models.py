from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=10)
    
    otp = models.CharField(max_length= 4,null=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return str(self.email)
    
    
class Verification(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=4)
    
    def __str__(self):
        return self.email