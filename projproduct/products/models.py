from django.db import models


class ProductDetails(models.Model):
    name = models.CharField(null=False, blank=False, max_length=128)
    price = models.PositiveIntegerField(null=False, blank=False)
    quantity = models.PositiveSmallIntegerField(null=False, blank=False)

    class Meta:
        db_table = 'product_details'
        ordering = ['-id']

    def __str__(self):
        return self.name