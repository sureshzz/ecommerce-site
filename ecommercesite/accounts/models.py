from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



class Myaccountmanager (BaseUserManager):
  def create_user(self,first_name,last_name,email,password = None):
    if not email:
      raise ValueError('Users must have an email address')
    if not password:
      raise ValueError('Users must have a password')
    
    user = self.model(
      first_name = first_name,
      last_name = last_name,
      email = self.normalize_email(email),
    )

    user.set_password(password)
    user.save(using = self._db)
    return user
  
  def create_superuser(self,first_name,last_name,email,username,password):
    user = self.create_user(
      first_name = first_name,
      last_name = last_name,
      email = self.normalize_email(email),
      username = username,
      password = password,
    )
    user.is_admin = True
    user.is_staff = True
    user.is_active = True
    user.is_superadmin = True
    user.save(using = self._db)
    return user
  


# Create your models here.
class Account(AbstractBaseUser):
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length = 50)
  username = models.CharField(max_length = 50,unique = True)
  email = models.EmailField(max_length = 100, unique = True)
  phone_number = models.CharField(max_length = 50)

#required 
  date_joined = models.DateField(auto_now_add = True)
  last_login = models.DateField(auto_now_add = True)
  is_admin = models.BooleanField(default = False)
  is_staff = models.BooleanField(default = False)
  is_active = models.BooleanField(default = False)
  is_superadmin = models.BooleanField(default = False)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS =   ['username','first_name','last_name']

  object = Myaccountmanager()

  def __str__(self):
    return self.email
  
  #whether the user has a specific permission (perm)
  # all admin users (is_admin=True) have all permissions
  def has_perm(self , perm , obj = None):
    return self.is_admin
  
  def has_module_perm(self,add_label): #the user has permission to add objects of a specific module 
    return True