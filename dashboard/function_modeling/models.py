from django.db import models

# Create your models here.
class Function(models.Model):
    id = models.CharField(max_length = 10, primary_key=True)
