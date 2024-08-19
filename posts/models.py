from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Define the custom user model
class CustomUser(AbstractUser):
    # Additional fields
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", blank=True, null=True
    )
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username


# Define the image model
class Image(models.Model):
    image = models.ImageField(upload_to="post_images/")
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.caption or "Image"


# Define the post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    images = models.ManyToManyField(Image, blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title
