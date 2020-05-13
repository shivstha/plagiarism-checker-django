from django.contrib import admin
from .models import Assignment, UploadedAssignment


class UploadAssignmentInline(admin.TabularInline):
    model = UploadedAssignment


class AssignmentAdmin(admin.ModelAdmin):
    inlines = [
        UploadAssignmentInline,
    ]
    list_display = ("title", "by_teacher", "date", "deadline")


admin.site.register(Assignment, AssignmentAdmin, )


@admin.register(UploadedAssignment)
class UploadedAssignmentAdmin(admin.ModelAdmin):
    list_display = ['assignment', 'student', 'uploaded_date']