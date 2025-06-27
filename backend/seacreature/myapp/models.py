from django.db import models
from django.contrib.auth.models import User


class CreatureCard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='creatures/', null=True, blank=True)
    discovered_on = models.DateField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creature = models.ForeignKey(CreatureCard, on_delete=models.CASCADE)
    visit_date = models.DateField()
    booking_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} booked {self.creature.name}"

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('M-Pesa', 'M-Pesa'),
        ('Tigo Pesa', 'Tigo Pesa'),
        ('Airtel Money', 'Airtel Money'),
        ('Card', 'Card'),
        ('Cash', 'Cash'),
    ]

    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    )

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"Payment {self.id} for Booking {self.booking.id}"
