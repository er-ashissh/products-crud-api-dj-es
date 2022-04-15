from django.db import models


class ProductDetailsv2(models.Model):
    name = models.CharField(null=False, blank=False, max_length=128)
    price = models.PositiveIntegerField(null=False, blank=False)
    quantity = models.PositiveSmallIntegerField(null=False, blank=False)

    class Meta:
        db_table = 'product_details_v2'
        ordering = ['-id']

    def __str__(self):
        return self.name