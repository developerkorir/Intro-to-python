from django.db import models


# Create your models here.
class Employee(models.Model):
    # name, email, dob, salary, disabled
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    disabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # added once during creation
    updated_at = models.DateTimeField(auto_now=True)  # updates every time update happens

    def __str__(self):
        return self.name
