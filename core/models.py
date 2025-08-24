from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project = models.CharField(max_length=100,null=True)
    phone_number = models.CharField(max_length=20, blank=True,null=True)

    def __str__(self):
        return f"{self.user.username} - {self.project}"
