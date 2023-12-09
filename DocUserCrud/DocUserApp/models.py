from django.db import models
from django.utils import timezone

class User(models.Model):
    email = models.CharField(max_length=255, blank=False)
    last_password_redefinition_at = models.DateTimeField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    password = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    last_update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        app_label = 'DocUserApp'

class Company(models.Model):
    name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    last_update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    locale = models.CharField(max_length=6, blank=False, default="PT")
    lang = models.CharField(max_length=10, blank=False, default="-03:00")
    
    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        app_label = 'DocUserApp'
    
class Doc(models.Model):
    name = models.CharField(max_length=255, blank=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    last_update_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    date_limit_to_sign = models.DateTimeField(null=True, blank=True)
    signed = models.BooleanField(default=False)

    created_by_user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    class Meta:
        app_label = 'DocUserApp'