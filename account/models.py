from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True  

    def create_user(self, email, password, name):
        if not email:
            raise "email x"
        if not password:
            raise "password x"
        
        user:CustomUser = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)        
        user.save(using=self._db)        
        return user
    
    def create_superuser(self, email, password):        
        user:CustomUser = self.create_user(            
            email = self.normalize_email(email),
            password=password,        
            name="admin"
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user 

class CustomUser(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    
    email = models.EmailField(blank=False, unique=True)
    name = models.CharField(max_length=20, blank=True, default="null")
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    
    def __str__(self):
       return self.email

    @property
    def is_staff(self):
        return self.is_admin
    
class Test(models.Model):
    number = models.IntegerField()