from django.db import models


class EmployeeDetails(models.Model):
    city = models.CharField(null=False, blank=False, max_length=128)
    age = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        db_table = 'employee_details'
        ordering = ['-id']

    def __str__(self):
        return self.city