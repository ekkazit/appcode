from django.contrib import admin

from .models import Video, VideoOption, VideoPlaylist, VideoRegister


class VideoOptionInline(admin.TabularInline):
    model = VideoOption
    extra = 0


class VideoPlaylistInline(admin.TabularInline):
    model = VideoPlaylist
    extra = 0


class VideoAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'teacher', 'lessons', 'price', 'published']
    search_fields = ['code', 'name']
    inlines = [VideoOptionInline, VideoPlaylistInline]


class VideoRegisterAdmin(admin.ModelAdmin):
    list_display = ['video', 'member', 'register_date', 'paid', 'paid_date', 'paid_via', 'authorized']
    list_filter = ['paid', 'authorized']


admin.site.register(Video, VideoAdmin)
admin.site.register( VideoRegister, VideoRegisterAdmin)
