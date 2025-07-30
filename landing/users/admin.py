from django.contrib import admin
from .models import Customers, Profile


# Register your models here.
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'biografy')


admin.site.register(Customers, CustomersAdmin)
admin.site.register(Profile, ProfileAdmin)
