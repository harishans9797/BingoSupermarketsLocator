from django.db import models



class ShopLocations(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    distance = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)



    class Meta:
        verbose_name_plural = "Bingo Supermarkets"

    def __str__(self):
        return self.name + ' ' + self.address

    def __float__(self):
        return self.distance + self.latitude + self.longitude


