from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Department(models.Model):
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

class Role(models.Model):
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name

class User(AbstractUser):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    dept = models.ForeignKey('Department', on_delete=models.CASCADE, null=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, null=True)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    date_of_joining = models.DateField(default=timezone.now) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  
        blank=True,
    )

    def __str__(self):
        return self.username

