from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from utils import ZONES

class Apartment(models.Model):
    zone = models.IntegerField(choices=ZONES, null=False)
    interior_area = models.IntegerField(validators=[MinValueValidator(65), MaxValueValidator(140)], null=False)
    # gross_area = models.DecimalField(max_digits=5, decimal_places=5, null=False)
    rooms = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], null=False)
    bathrooms = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)], null=False)

    class Meta:
        app_label = "apartments"
