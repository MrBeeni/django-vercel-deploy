from django.db import models
import uuid

# Create your models here.


class Company(models.Model):
    company_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    ceo = models.CharField(max_length=100)
    employees = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    company_type = models.CharField(
        max_length=100, choices=(('IT', 'IT'), ('Mobile', 'Mobile')))

    def __str__(self):
        return self.name


class Employee (models.Model):
    employee_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
