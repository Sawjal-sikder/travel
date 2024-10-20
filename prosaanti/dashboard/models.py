from django.db import models


class CompanyInformation(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the company")
    address = models.TextField(help_text="Company's address")
    phone_number = models.CharField(max_length=15, help_text="Contact phone number")
    email = models.EmailField(help_text="Company email address")
    website = models.URLField(blank=True, null=True, help_text="Company website URL")
    tax_id = models.CharField(max_length=50, blank=True, null=True, help_text="Company tax identification number")
    icon = models.ImageField(upload_to='company_logos/', blank=True, null=True, help_text="Company icon")
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True, help_text="Company logo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"

    def __str__(self):
        return self.name
