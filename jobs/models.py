from django.db import models

from django.contrib.auth.hashers import make_password


class PostJob(models.Model):
    title = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    companyName = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    jobType = models.CharField(max_length=255)
    url = models.URLField(max_length=1500)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        # Hash password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def _str_(self):
        return self.name
