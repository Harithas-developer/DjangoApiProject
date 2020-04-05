from django.db import models

# Create your models here.

class Name(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class AcitvityPeriod(models.Model):
    data = models.TextField(max_length=300 , blank=True)
    name = models.ForeignKey(Name, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.data




