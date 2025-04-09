from django.db import models

# Create your models here.
class Objects(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    address = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    map = models.JSONField(null=False, default=dict, blank=True)
    image = models.FileField(upload_to="images",null=False)
    tags = models.JSONField(null=False, blank=True, default=list)
    price = models.IntegerField(blank=True)
    time = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name
