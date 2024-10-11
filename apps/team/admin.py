from django.contrib import admin

# Register your models here.

from .models import Invitation, Team

admin.site.register(Team)
admin.site.register(Invitation)
