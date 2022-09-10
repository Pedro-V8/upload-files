from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class AdminDocuments(admin.ModelAdmin):

    fields = ("first_name" , "last_name" , "age" , "username" , "email" , "password" , "is_active" , "is_staff" , "user_permissions" , "groups")
    
    list_display = ("id","first_name" , "last_name" , "age" , "username" , "email" , "password" , "is_active" , "is_staff")
