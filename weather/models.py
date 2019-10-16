from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)


    def __str__(self):
        return "{}, {}".format(self.name, self.state)


class User(models.Model):
    email = models.EmailField(unique = True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.email + ":" + str(self.location)