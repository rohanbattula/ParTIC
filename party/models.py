from django.db import models

# Create your models here.
class Party(models.Model):
    # put characteristics of party here
    name = models.CharField(max_length = 100, unique=True)
    address = models.CharField(max_length = 1000)
    status = models.BooleanField()
    distance = models.DecimalField(decimal_places = 2, max_digits = 4)
    entryFee = models.IntegerField()
    dateTime = models.DateTimeField()
    guysAllowed = models.BooleanField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 20, unique=False)
    age = models.IntegerField()
    email = models.CharField(max_length = 100, )
    profilePic = models.ImageField(upload_to="party/", null=True, blank=True)

    def __str__(self):
        return self.profilePic
        return self.name
