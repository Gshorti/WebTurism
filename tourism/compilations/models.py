from django.db import models

class Compilation(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    data = models.JSONField(null=False, blank=False, default=list)
    
