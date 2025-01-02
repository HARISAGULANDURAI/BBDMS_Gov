from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPES = [
        (1, 'Admin'),
        (2, 'Donor'),
        (3, 'Requester'),
    ]
    user_type = models.CharField(choices=USER_TYPES, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='media/profile_pic', null=True, blank=True)
    email_verified = models.BooleanField(default=False)  # New field to track email verification


class Bloodgroup(models.Model):
    bloodgroup = models.CharField(max_length=200, unique=True)  # Added uniqueness for blood groups
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bloodgroup  # Makes it easier to display in the admin panel


class DonorReg(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    age = models.PositiveIntegerField(default=0)  # Changed to PositiveIntegerField
    mobile_number = models.CharField(max_length=11)
    bloodgroup = models.ForeignKey(Bloodgroup, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])  # Added choices
    address = models.TextField(max_length=500)  # Changed to TextField for flexibility
    status = models.CharField(max_length=50, default='Pending')  # Changed default to 'Pending' for clarity
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Unregistered Donor'} - {self.bloodgroup}"


class BloodRequest(models.Model):
    donor = models.ForeignKey(DonorReg, on_delete=models.SET_NULL, null=True)  # Changed to SET_NULL for flexibility
    full_name = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=250)
    requester = models.CharField(max_length=250)  # Renamed for consistency
    message = models.TextField(max_length=1000)  # Increased max_length for message
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Request by {self.full_name} - {self.requester}"


class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=250)
    message = models.TextField(max_length=1000)  # Increased max_length for message
    status = models.CharField(max_length=50, default='Pending')  # Added default status
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Contact from {self.full_name}"
