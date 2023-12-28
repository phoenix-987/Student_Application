from django.db import models


# Create your models here.
class StudentData(models.Model):
    id = models.CharField(primary_key=True, max_length=5, blank=False, null=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    age = models.IntegerField(blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
