from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=250, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to=True, blank=True)

    
