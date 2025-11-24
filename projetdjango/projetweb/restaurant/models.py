from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('employe', 'Employé'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('employe', 'Employé'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)