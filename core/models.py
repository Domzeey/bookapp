from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ManyToManyField(Author)
    published_date = models.DateTimeField(default=timezone.now)
    cover_image = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return self.title
