# Generated by Django 5.2 on 2025-04-03 08:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('service', models.CharField(choices=[('digital_marketing', 'Digital Marketing'), ('social_media', 'Social Media Marketing'), ('seo', 'SEO'), ('google_ads', 'Google Ads'), ('web_design', 'Website Designing')], max_length=50)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
