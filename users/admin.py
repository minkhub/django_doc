from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    con_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)