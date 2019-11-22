from django.contrib import admin
from django.contrib.auth.models import *
from .models import User, KCustomer
# Register your models here.
admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(KCustomer)