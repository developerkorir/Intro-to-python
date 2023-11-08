from django.db import models


# Create your models here.
class Employee(models.Model):
    # name, email, dob, salary, disabled
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True)
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    disabled = models.BooleanField(default=False)
    profile = models.ImageField(upload_to="employees", null=True, default="employees/default.png")
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # added once during creation
    updated_at = models.DateTimeField(auto_now=True, null=True)  # updates every time update happens

    def __str__(self):
        return self.name
