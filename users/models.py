from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    bio = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to="media/images/%Y/%m")
    birthday = models.DateField(auto_now=False)
    blog_url = models.URLField(max_length = 60, blank=True)