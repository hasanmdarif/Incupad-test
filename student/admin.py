from django.contrib import admin
from .models import Student, markList
from import_export.admin import ExportActionMixin
class StudentAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('studentId', 'fullName', 'email')
    


admin.site.register(Student, StudentAdmin)


class MarkAdmin(admin.ModelAdmin):
    list_display = ('studentId', 'studentName')
    search_fields = ['studentId', 'studentName']


admin.site.register(markList, MarkAdmin)
