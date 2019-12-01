from django.contrib import admin
from django.contrib.auth.models import *
from .kmodels.user_model import User
from .kmodels.customer_model import KCustomer

# Register your models here.
admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(KCustomer)