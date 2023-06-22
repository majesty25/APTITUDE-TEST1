from django.conf import settings
from django.db import models
from rest_framework import fields


class Diagnosis(models.Model):
    """Diagnosis object"""
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    null=True
    )
    category = models.ManyToManyField('Category')
    Diagnosis_code = models.CharField(max_length=255)
    Full_code = models.CharField(max_length=255, blank=True, null=True)
    Abbreviated_description = models.TextField(blank=True)
    Full_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.name  
    
class Category(models.Model): 
    """Category object"""
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    null=True
    )
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.title}'
    