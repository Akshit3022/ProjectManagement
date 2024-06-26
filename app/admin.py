from django.contrib import admin
from app.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserModelAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["id", "email", "name", "userType", "is_active", "is_admin", "allocation_percentage"]
    list_filter = ["is_admin"]
    fieldsets = [
        ('User Credential', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "userType"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "userType", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []


# Now register the new UserAdmin...
    
admin.site.register(CustomUser, UserModelAdmin)

class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ["project_id","projectCreator", "projectName", "projectDescription", "projectStartDate"]
admin.site.register(Project, ProjectModelAdmin)

class ProjectAllocationModelAdmin(admin.ModelAdmin):
    list_display = ["emp_allocation","project"]
admin.site.register(ProjectAllocation, ProjectAllocationModelAdmin)

class ManageLeaveModelAdmin(admin.ModelAdmin):
    list_display = ["empName","leaveType","leaveReason", "notifyTo"]
admin.site.register(ManageLeave, ManageLeaveModelAdmin)

class SalaryPaymentModelAdmin(admin.ModelAdmin):
    list_display = ["user","amount","payment_date","payment_method"]
admin.site.register(SalaryPayment, SalaryPaymentModelAdmin)