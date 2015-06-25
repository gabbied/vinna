from django.contrib import admin

from .models import Company
class CompanyDetails(admin.ModelAdmin):
	fields = ['company_name', 'company_description', 'company_address', 'company_number', 'company_contact_person']

admin.site.register(Company, CompanyDetails)