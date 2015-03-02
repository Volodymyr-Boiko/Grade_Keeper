from django.contrib import admin
from Grade_Keeper_app.models import *


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'e_mail')


admin.site.register(Student, StudentAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'due_date', 'points_possible')


admin.site.register(Assignments, AssignmentAdmin)


class PointsAdmin(admin.ModelAdmin):
    list_display = ('students', 'points')
