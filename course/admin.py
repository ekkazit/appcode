from django.contrib import admin

from .models import (
    Course,
    CourseOption,
    CourseSlider,
    CourseOpen,
    CourseBooking,
    CourseRegister,
    Quotation,
)


class CourseOptionInline(admin.TabularInline):
    model = CourseOption
    extra = 0


class CourseSliderInline(admin.TabularInline):
    model = CourseSlider
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'hours', 'days', 'price', 'published']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug': ['name']}
    inlines = [CourseOptionInline, CourseSliderInline]


class CourseOpenAdmin(admin.ModelAdmin):
    list_display = ['name', 'times', 'location', 'price', 'published', 'finished']
    list_filter = ['published', 'finished']
    search_fields = ['name']


class CourseBookingAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'email', 'phone', 'company', 'booking_date', 'completed']
    list_filter = ['completed']
    search_fields = ['name', 'email']


class CourseRegisterAdmin(admin.ModelAdmin):
    list_display = ['course_open', 'name', 'email', 'phone', 'company', 'persons', 'reg_date', 'paid', 'completed']
    list_filter = ['paid', 'completed']
    search_fields = ['name', 'email']


class QuotationAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'email', 'phone', 'company', 'completed']
    list_filter = ['completed']
    search_fields = ['name', 'email']


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseOpen, CourseOpenAdmin)
admin.site.register(CourseBooking, CourseBookingAdmin)
admin.site.register(CourseRegister, CourseRegisterAdmin)
admin.site.register(Quotation, QuotationAdmin)
