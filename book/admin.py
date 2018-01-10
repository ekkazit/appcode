from django.contrib import admin

from .models import Book, BookOption, Register


class BookOptionInline(admin.TabularInline):
    model = BookOption
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'pages', 'years', 'price', 'published']
    search_fields = ['code', 'name']
    prepopulated_fields = {'slug': ['name']}
    inlines = [BookOptionInline]


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['book', 'name', 'phone', 'email', 'paid', 'paid_date', 'delivered']
    list_filter = ['paid', 'delivered']
    search_fields = ['name', 'email', 'phone']


admin.site.register(Book, BookAdmin)
admin.site.register(Register, RegisterAdmin)
