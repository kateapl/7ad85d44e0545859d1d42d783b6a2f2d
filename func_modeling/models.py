
from django.db import models

# Create your models here.
class Function(models.Model):
    function = models.CharField(max_length = 10)
    graph = models.CharField(max_length = 10)
    interval = models.IntegerField(default=1)
    step = models.IntegerField(default=1)
    date = models.DateTimeField(default=1)