# Generated by Django 4.2.15 on 2024-10-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinformation',
            name='is_new',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
