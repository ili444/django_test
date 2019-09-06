from django.db import models

class Post(models.Model):
    url = models.URLField(blank=False)
    timeshift = models.PositiveIntegerField(default=0)
    success = models.BooleanField(default=False)
    time = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=150, blank=True, default='', null=True)
    h1 = models.CharField(max_length=150, blank=True, default='', null=True)
    encode = models.CharField(max_length=16, blank=True, default='', null=True)


