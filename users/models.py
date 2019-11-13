from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from model_utils import Choices
from django.utils.translation import gettext as _
from multiselectfield import MultiSelectField

def nameFile(instance, filename):
    imgpath= '/'.join(['images', str(instance.source), filename])
    return imgpath

class UserType(models.Model):    
    user_type= models.CharField(null=True, max_length=80,  default=None)  
    description = models.CharField(max_length=150, blank=True, null=True)
    class Meta:
        db_table = 'user_type'
        managed = True
        verbose_name = 'user_type'
        verbose_name_plural = 'user_types'
    
    def __str__(self):
        return self.user_type

class File(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=nameFile, max_length=254, blank=True, null=True)
    source = models.CharField(blank=True, null=True, default='customer', max_length=50)
    size = models.IntegerField(blank=True, null=True, default=0)
    class Meta:
        db_table = 'file'
        managed = True

    def __str__(self):
        return self.file.name

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, userName, phone, user_type='CUSTOMER', user_role='GUEST', email=None, password=None, images=None):
        if not phone:
            raise ValueError('Users must have an Phone number')
           
        user = self.model(
            userName = userName,
            phone = phone,
            email = self.normalize_email(email),
            user_type = user_type,
            user_role= user_role,
            images=images
        )
        user.set_password(password)
        
        user.is_admin =False
        user.is_active =True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userName=None, phone=None, user_type='CUSTOMER', user_role='GUEST', email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        user = self.create_user(userName, phone, email=email, password=password)
        user.is_admin = True 
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    USER_ROLE = Choices(
        ('USER', 'USER'),
        ('ADMIN', 'ADMIN'),
        ('LEADER', 'LEADER'),
        ('SUPER_ADMIN', 'SUPER ADMIN'),
        ('GUEST', 'GUEST'),
        ('DEL_BOY', 'DELIVERY BOY'),
    )
    userName = models.CharField("User Name", max_length=50, unique=True)
    images = models.ForeignKey(File, on_delete=models.CASCADE, default=None, blank=True, null=True)
    phone = models.CharField("Phone Number", max_length=50, unique=True)
    email = models.EmailField("Email Address", blank=True, null= True)
    password = models.CharField('password', max_length=128, null=False)
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE, default=None, null=False)
    user_role = models.CharField(max_length=80, choices=USER_ROLE, default=USER_ROLE.GUEST)
    
    is_admin = models.IntegerField(default=False)
    is_staff = models.IntegerField(default=False)
    is_active = models.IntegerField(default=False)
    is_superuser = models.IntegerField(default=False)

    objects = UserManager()

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['userName', 'user_type', 'user_role']

    class Meta:
        db_table = 'user'
        managed = True
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.phone

    def __unicode__(self):
        return 

class Address(models.Model):
    address_line_1= models.CharField(default='', max_length=50)
    address_line_2= models.CharField(max_length=50, null=True)
    landmark= models.CharField(max_length=50, null=True)
    postalCode= models.IntegerField(null=True)
    latitude= models.FloatField(max_length=20, null=True)
    longitude= models.FloatField(max_length=20, null=True)
    geoAddress= models.CharField(max_length=100, null=True)
    city= models.CharField(max_length=25, null=True)
    state= models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)
    
    class Meta:
        db_table = 'address'
        managed = True
        verbose_name = 'address'
        verbose_name_plural = 'addresses'
    
    def __str__(self):
        return self.landmark

# Create your models here.
class Customer(models.Model):
    name= models.CharField(null=True, max_length=80,  default=None)  
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'customer'
        managed = True
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    
    def __str__(self):
        return self.userName


class Tailor(models.Model):
    name= models.CharField(null=True, max_length=80,  default=None)
    
    start_time = models.DateTimeField(default=now, editable=False)
    end_time = models.DateTimeField(default=now, editable=False)
    masters_count = models.IntegerField(blank=True, null=True, default=None)
    is_weekends = models.BooleanField(default=False, blank=True, null=True)
    is_weekdays = models.BooleanField(default=True, blank=True, null=True)
    alternate_days = models.CharField(max_length=20, blank=True, null=True)
    is_open = models.BooleanField(default=False)
    is_emergency_available = models.BooleanField(default=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'tailor'
        managed = True
    
    def __str__(self):
        return self.shopName


class Boutique(models.Model):
    name= models.CharField(null=True, max_length=80,  default=None)  
    
    start_time = models.DateTimeField(default=now, editable=False)
    end_time = models.DateTimeField(default=now, editable=False)
    masters_count = models.IntegerField(blank=True, null=True, default=None)
    is_weekends = models.BooleanField(default=False, blank=True, null=True)
    is_weekdays = models.BooleanField(default=True, blank=True, null=True)
    alternate_days = models.CharField(max_length=20, blank=True, null=True)
    is_open = models.BooleanField(default=False)
    is_emergency_available = models.BooleanField(default=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'boutique'
        managed = True
        verbose_name = 'Boutique'
        verbose_name_plural = 'boutiques'
    
    def __str__(self):
        return self.shopName


class MaggamDesigner(models.Model):  
    name= models.CharField(null=True, max_length=80,  default=None)  
    
    freelancer = models.BooleanField(default=False)
    working_in = models.CharField(max_length=50, blank=True, null=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'maggamDesigner'
        managed = True
        verbose_name = 'maggamDesigner'
        verbose_name_plural = 'maggamDesigners'
    
    def __str__(self):
        return self.shopName


class FashionDesigner(models.Model):    
    name= models.CharField(null=True, max_length=80,  default=None)  
    
    freelancer = models.BooleanField(default=False)
    working_in = models.CharField(max_length=50, blank=True, null=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'fashionDesigner'
        managed = True
        verbose_name = 'fashionDesigner'
        verbose_name_plural = 'fashionDesigners'
    
    def __str__(self):
        return self.shopName

class Master(models.Model):    
    name= models.CharField(null=True, max_length=80,  default=None)  
    
    available_days = models.CharField(max_length=20, blank=True, null=True)
    can_hire = models.BooleanField(default=False)
    working_in = models.CharField(max_length=50, blank=True, null=True)
    is_emergency_available = models.BooleanField(default=False)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'master'
        managed = True
        verbose_name = 'master'
        verbose_name_plural = 'masters'
    
    def __str__(self):
        return self.shopName









