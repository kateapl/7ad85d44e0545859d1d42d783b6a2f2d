import datetime
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

# Create your models here.
class Function(models.Model):
    function = models.CharField(max_length = 10)
    graph = models.ImageField(blank=True, default='default.jpg', help_text='150x150px')
    interval = models.IntegerField(default=1)
    step = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.function}"

    def image(self):
        if self.graph:
            return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % self.graph.url)
        else:
            return '(Нет изображения)'

    image.short_description = 'Картинка'
    image.allow_tags = True

    def exception_text(self):
        """write error text instead of image"""

    def add_graph(self):
        """add graph in db"""
        #make_graph(self.id,self.function, self.interval, self.step)
        