from django.contrib import admin
from .models import User, IP_address, status 

# Register your models here.


admin.site.register(User)
admin.site.register(IP_address)
admin.site.register(status)
