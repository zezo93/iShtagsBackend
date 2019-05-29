from django.contrib import admin
from .models import Tag, Category


# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at', 'updated_at')


admin.site.register(Tag, TagAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')


admin.site.register(Category, CategoryAdmin)
