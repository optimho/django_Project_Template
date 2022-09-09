from django.db import models


# Create your models here.
class User_List(models.Model):

    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()

    def __str__(self):
        return (self.first_name)
