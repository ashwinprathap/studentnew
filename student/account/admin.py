from django.contrib import admin
from.models import Contact,Course,Staff

# Register your models here.
from .models import Course
admin.site.register(Course)

class Customerdetails(admin.ModelAdmin):
    list_display=('name','phno','email')
admin.site.register(Contact,Customerdetails)

admin.site.register(Staff)
