from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, userName, phone, email=None, password=None):
        if not phone:
            raise ValueError('Users must have an Phone number')
           
        user = self.model(
            userName = userName,
            phone = phone,
            email = self.normalize_email(email)
        )
        
        user.is_admin =False
        user.is_active =True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userName=None, phone=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        user = self.create_user(userName, phone, email=email, password=password)
        user.is_admin = True 
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    userName = models.CharField("User Name", max_length=50, unique=True)
    phone = models.CharField("Phone Number", max_length=50, unique=True)
    email = models.EmailField("Email Address", blank=True, null= True)
    password = models.CharField('password', max_length=128, null=False)
    
    ''' Roles here '''
    is_customer= models.BooleanField('User is Customer', default=False)
    is_tailor= models.BooleanField('User is Tailor', default=False)
    is_master= models.BooleanField('User is Master', default=False)
    is_maggam_designer= models.BooleanField('User is Maggam Designer', default=False)
    is_fashion_designer= models.BooleanField('User is Fashion Designer', default=False)
    is_boutique= models.BooleanField('User is Boutique', default=False)
    
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
    REQUIRED_FIELDS = ['userName' ]

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
    name= models.CharField(null=True, max_length=80)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, default=True)
    address= models.ManyToManyField(Address)
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
    name= models.CharField(null=True, max_length=80)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, default=True)
    address= models.ForeignKey(Address, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'tailor'
        managed = True
        verbose_name = 'Tailor'
        verbose_name_plural = 'tailors'
    
    def __str__(self):
        return self.shopName


class Boutique(models.Model):
    name= models.CharField(null=True, max_length=80)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, default=True)
    address= models.ForeignKey(Address, on_delete=models.CASCADE)
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
    name= models.CharField(null=True, max_length=80)  
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, default=True)
    address= models.ForeignKey(Address, on_delete=models.CASCADE)
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
    firmName= models.CharField(null=True, max_length=80)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, default=True)
    address= models.ForeignKey(Address, on_delete=models.CASCADE)
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
    name= models.CharField(null=True, max_length=80)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, default=True)
    address= models.ForeignKey(Address, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'master'
        managed = True
        verbose_name = 'master'
        verbose_name_plural = 'masters'
    
    def __str__(self):
        return self.shopName

