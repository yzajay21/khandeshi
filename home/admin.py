from django.contrib import admin
from .models import RegisterProfile
# Register your models here.

class RegisterProfileAdmin(admin.ModelAdmin):
	list_display = ['first_name','last_name','mobile_no','blood_group','Profession',]
admin.site.register(RegisterProfile,RegisterProfileAdmin)