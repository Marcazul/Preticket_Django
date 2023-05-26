from django.db import models

# Create your models here.

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    contract_number = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Contract(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contract_number = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.contract_number

class Revenue(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.company.name} - {self.year}"
