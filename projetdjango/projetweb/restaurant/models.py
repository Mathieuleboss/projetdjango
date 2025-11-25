from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# ======================== PROFILE ========================
class Profile(models.Model):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('employe', 'Employé'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return f"{self.user.username} - {self.role}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# ======================== TABLE ========================
class Table(models.Model):
    number = models.PositiveIntegerField()
    seats = models.PositiveIntegerField(default=4)

    def __str__(self):
        return f"Table {self.number} ({self.seats} places)"


# ======================== RESERVATION ========================
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - Table {self.table.number} on {self.date} at {self.time}"
