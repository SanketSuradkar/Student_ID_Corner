from django.contrib import admin
from .models import Student
# this admin code is usend to add the  emial name and the id of the perticula targated student and the customer or the end user 
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]

