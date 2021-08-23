import datetime
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


# Create your models here.
class Function(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='id')
    function = models.CharField(max_length=10)
    graph = models.ImageField(blank=True, default='default.jpg', help_text='150x150px')
    interval = models.IntegerField(default=1)
    step = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.function}"

    def image(self):
        # from .tasks import make_graph
        # try:
        #     self.graph = make_graph.delay(self.id).result
        # except Exception as e:
        #     return str(e)
        return mark_safe('<img src="%s" style="width: 145px; height:145px;" />' % self.graph.url)

    image.short_description = 'Картинка'
    image.allow_tags = True

    def exception_text(self):
        """write error text instead of image"""

        