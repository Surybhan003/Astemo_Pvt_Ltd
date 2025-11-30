from django.db import models

class Person(models.Model):
    BLOOD_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.FloatField(help_text="Weight in kg")
    created_at = models.DateTimeField(auto_now_add=True)
    edit_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.blood_group})"
