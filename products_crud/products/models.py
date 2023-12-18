# products/models.py
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    rating = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_star_range(self):
        new_rating = max(1, min(int(self.rating), 5))
        return range(new_rating)
