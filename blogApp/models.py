

from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from users.models import User


class Blog(models.Model):

    Status_Choice = (
        ('DRAFT0', 'Draft'),
        ('PUBLISHED', 'Published')
    )

    title = models.CharField(max_length=20, null=False, blank=True)
    content = models.TextField(max_length=100, null=True, blank=False)
    user_id = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, null=False, blank=False, choices=Status_Choice, default='ACTIVE')
    created_at = models.TimeField(auto_now=timezone.now)
    update_at = models.TimeField(auto_now=timezone.now)








