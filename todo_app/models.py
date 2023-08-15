from django.db import models

# Create your models here.
class TodoWorkModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    status = models.BooleanField(default=False)
