from django.db import models
from datetime import datetime
from django.utils.timezone import now


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
    fullName= models.CharField(default='',max_length=50, null=False)
    userName= models.CharField(default='',max_length=50, null=False)
    email= models.EmailField(max_length=50, null=True)
    mobileNo= models.IntegerField(null=True)
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
    fullName= models.CharField(default='',max_length=50, null=False)
    shopName= models.CharField(max_length=50, null=True)
    userName= models.CharField(default='',max_length=50, null=False)
    email= models.EmailField(max_length=50, null=True)
    mobileNo= models.IntegerField(null=True)
    address= models.ManyToManyField(Address)
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
    fullName= models.CharField(default='',max_length=50, null=False)
    shopName= models.CharField(max_length=50, null=True)
    userName= models.CharField(default='',max_length=50, null=False)
    email= models.EmailField(max_length=50, null=True)
    mobileNo= models.IntegerField(null=True)
    address= models.ManyToManyField(Address)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'boutique'
        managed = True
        verbose_name = 'Boutique'
        verbose_name_plural = 'boutiques'
    
    def __str__(self):
        return self.shopName


class Designer(models.Model):
    fullName= models.CharField(default='', max_length=50, null=False)
    shopName= models.CharField(max_length=50, null=True)
    userName= models.CharField(default='',max_length=50, null=False)
    email= models.EmailField(max_length=50, null=True)
    mobileNo= models.IntegerField(null=True)
    address= models.ManyToManyField(Address)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'designer'
        managed = True
        verbose_name = 'designer'
        verbose_name_plural = 'designers'
    
    def __str__(self):
        return self.shopName


