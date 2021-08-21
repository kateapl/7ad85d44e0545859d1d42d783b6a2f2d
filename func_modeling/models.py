import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Function(models.Model):
    function = models.CharField(max_length = 10)
    graph = models.ImageField(default='default.jpg')
    interval = models.IntegerField(default=1)
    step = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.function}"

    def exception_text(self):
        """write error text instead of image"""