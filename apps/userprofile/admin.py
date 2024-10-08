from django.contrib import admin

from apps.userprofile.models import UserProfile

# Register your models here.
from .models import UserProfile

admin.site.register(UserProfile)
