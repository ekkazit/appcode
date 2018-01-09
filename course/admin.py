from django.contrib import admin

from .models import Course, CourseOption, CourseSlider


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


admin.site.register(Course, CourseAdmin)
