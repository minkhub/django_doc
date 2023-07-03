from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.urls import reverse_lazy, reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    profile_photo = models.ImageField(null=True, blank=True, upload_to='profile_images/')
    note = models.TextField(blank=True, help_text="자기소개를 작성하세요", editable=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def get_absolute_url(self):
        return reverse('user:profile', args=[self.pk])
    
    def get_image_url(self):
        return '%s%s' %(settings.MEDIA_URL, self.profile_photo)
    

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user.username} - {self.content}"