from django.contrib import admin
from .models import UserData, AccountDetails
# Register your models here.

class UserDataAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)} 

admin.site.register(UserData)
admin.site.register(AccountDetails)

