from django.db import models

# Create your models here.
class Party(models.Model):
    # put characteristics of party here
    name = models.charField(max_length = 100, unique=True)
    address = models.charField(max_length = 1000)
    status = models.BooleanField()
    distance = models.DecimalField()
    entryFee = models.IntegerField()
    dateTime = models.DateTimeField()
    guysAllowed = models.BooleanField()

   def __str__(self):
        return self.name
