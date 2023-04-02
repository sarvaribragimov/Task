from django.contrib import admin
from .models import Group,Student,Student_information,Organization_address,Organization_name,Level
# Register your models here.
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Student_information)
admin.site.register(Organization_name)
admin.site.register(Level)
admin.site.register(Organization_address)