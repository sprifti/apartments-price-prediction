from django.db import models


class Predictions(models.Model):
    apartment = models.ForeignKey(
        to="Apartment", null=True, on_delete=models.SET_NULL
    )
    predicted_price = models.DecimalField(max_digits=40, decimal_places=20, null=False)
    accurate_price = models.BooleanField(null=True)

    class Meta:
        app_label = "apartments"
