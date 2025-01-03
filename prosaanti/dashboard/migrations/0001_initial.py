# Generated by Django 4.2.15 on 2024-10-20 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the company', max_length=255)),
                ('address', models.TextField(help_text="Company's address")),
                ('phone_number', models.CharField(help_text='Contact phone number', max_length=15)),
                ('email', models.EmailField(help_text='Company email address', max_length=254)),
                ('website', models.URLField(blank=True, help_text='Company website URL', null=True)),
                ('tax_id', models.CharField(blank=True, help_text='Company tax identification number', max_length=50, null=True)),
                ('icon', models.ImageField(blank=True, help_text='Company icon', null=True, upload_to='company_logos/')),
                ('logo', models.ImageField(blank=True, help_text='Company logo', null=True, upload_to='company_logos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Company Information',
                'verbose_name_plural': 'Company Information',
            },
        ),
    ]
