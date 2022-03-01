from django.db import models


class Music(models.Model):
    name = models.CharField(max_length=200)
    src = models.CharField(default='',max_length=200)
    pub_date = models.DateTimeField('date published')