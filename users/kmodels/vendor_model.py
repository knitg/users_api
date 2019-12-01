from django.db import models
from datetime import datetime
from django.conf import settings
from django.utils.timezone import now
from .address_model import KAddress
from .user_model import User
 
class KVendorUser(models.Model):
    name= models.CharField(null=True, max_length=80,  default=None)
    
    start_time = models.DateTimeField(default=now, editable=False)
    end_time = models.DateTimeField(default=now, editable=False)
    masters_count = models.IntegerField(blank=True, null=True, default=None)
    is_weekends = models.BooleanField(default=False, blank=True, null=True)
    is_weekdays = models.BooleanField(default=True, blank=True, null=True)
    alternate_days = models.CharField(max_length=20, blank=True, null=True)
    is_open = models.BooleanField(default=False)
    is_emergency_available = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False)
    address = models.ForeignKey(KAddress, on_delete=models.CASCADE, default=None, null=True)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now, editable=False)

    class Meta:
        db_table = 'knit_vendor_user'
        managed = True
    
    def __str__(self):
        return self.name
