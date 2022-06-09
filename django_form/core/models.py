from django.db import models


# Create your models here.
class Profile(models.Model):
    fname = models.TextField()
    lname = models.TextField()
    email = models.EmailField()
    pnumber = models.CharField(max_length= 12)
    password = models.CharField(max_length= 20)

    def __str__(self):
        return self.fname
