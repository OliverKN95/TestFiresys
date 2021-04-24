from django.contrib import admin
from .models import person, test

# Register your models here.
@admin.register(test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ['name']

# Register your models here.
@admin.register(person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address')
    list_filter = ('first_name', 'last_name')
    search_fields = ['first_name', 'last_name']