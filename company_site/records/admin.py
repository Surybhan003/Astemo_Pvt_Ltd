from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','age','blood_group','gender','weight','created_at')
    list_filter = ('blood_group','gender')
    search_fields = ('name',)
