import os
import uuid

from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from django.db import models

from like.models import Like


def get_image_path(instance, filename):
    return os.path.join('photo-profile', str(instance.user.username), filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    slug = models.SlugField(unique=True, editable=False, default=uuid.uuid4)
    image = models.ImageField(upload_to=get_image_path)
    description = models.CharField(max_length=256, blank=True)
    likes = GenericRelation(Like)
    pub_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}\'s post | {self.pub_time.date()}({self.pub_time.hour}:{self.pub_time.minute})'

    @property
    def total_likes(self):
        return self.likes.count()
