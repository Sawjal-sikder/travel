from django.contrib import admin
from .models import CompanyInformation


@admin.register(CompanyInformation)
class CompanyInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'website', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone_number')
