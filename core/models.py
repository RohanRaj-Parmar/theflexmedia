from django.db import models
from django.utils import timezone

class CustomerRequest(models.Model):
    SERVICE_CHOICES = [
        ('digital_marketing', 'Digital Marketing'),
        ('social_media', 'Social Media Marketing'),
        ('seo', 'SEO'),
        ('google_ads', 'Google Ads'),
        ('web_design', 'Website Designing'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.service} ({self.created_at.strftime('%Y-%m-%d')})"
    
    class Meta:
        ordering = ['-created_at']