from django.contrib import admin
from .models import test

# Register your models here.
@admin.register(test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ['name']