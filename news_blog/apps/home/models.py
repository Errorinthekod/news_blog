from django.db import models

from django.db import models

# Create your models here.

# Create your models here.


class About(models.Model):
    text = models.TextField('Текст')
    text2 = models.TextField('Текст2', blank=True, null=True)
    text3 = models.TextField('Текст3', blank=True, null=True)