from django.contrib import admin

from .models import Account, Category, Teacher, Member


class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'bank', 'branch', 'acc_code', 'acc_name', 'acc_type']
    search_fields = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    search_fields = ['name']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'fullname', 'position']
    search_fields = ['name']


class MemberAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'fullname', 'email']
    search_fields = ['code', 'name']


admin.site.register(Account, AccountAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Member, MemberAdmin)
