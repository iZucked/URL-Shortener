from django.db import models

# Create your models here.

class Visitor(models.Model):
    ip_addr = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=200)
    visit_time = models.DateTimeField(auto_now=True)
class URL(models.Model):
    linked_url = models.URLField(max_length=200)
    shortened_code = models.CharField(unique=True, max_length=100)
    creation_time = models.DateTimeField(auto_now=True)
    visitors = models.ManyToManyField(Visitor, blank=True)
    qr_code = models.CharField(max_length=500)
    is_password_protected = models.BooleanField()
    can_expire = models.BooleanField()
    password = models.CharField(blank=True, max_length=100, default=None)
    expiration_time = models.DateTimeField(blank=True, default=None)

