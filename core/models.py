from django.db import models


class Product(models.Model):
    AVAILABILITY_CHOICES = [
        ("In Stock", "In Stock"),
        ("Out of Stock", "Out of Stock"),
    ]

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="uploads/", blank=True, null=True)
    availability = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES, default="In Stock")
    grade = models.CharField(max_length=50, blank=True)
    rating = models.FloatField(default=5.0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=150, blank=True)
    place = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=50)
    grade = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.email})"
