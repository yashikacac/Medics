from django.db import models

# Create your models here.
class Input(models.Model):
    location = models.CharField(max_length = 50)

    def __str__(self):
        return self.location

class Hospital(models.Model):
    Name = models.TextField()
    Address = models.TextField()
    Locality = models.CharField(max_length = 50, default = Address)
    City = models.CharField(max_length = 50)
    State = models.CharField(max_length = 50)
    Oxygen_Cylinder = models.IntegerField(default = 0)
    Beds = models.IntegerField(default = 0)
    MRI_Machine = models.IntegerField(default = 0)

    def __str__(self):
        return self.Name

