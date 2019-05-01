from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogPost(models.Model):

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)

    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)
