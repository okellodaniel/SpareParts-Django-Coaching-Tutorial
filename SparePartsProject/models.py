from django.db import models

# Create your models here.
# Spare part model
class SparePart(models.Model):
    part_name = models.CharField(max_length=100)
    part_number = models.CharField(max_length=100, unique=True)
    arrival_date = models.DateField()
    total_initial_stock_quantity = models.IntegerField()
    country_of_origin = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.part_name
    
# Part Sales model
class PartSales(models.Model):
    buyer_names = models.CharField(max_length=100)
    buyer_contact = models.CharField(max_length=100)
    bought_part = models.CharField(max_length=100)
    date = models.DateField()
    number_of_items_taken = models.IntegerField()
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    part_name = models.CharField(max_length=100)

    def __str__(self):
        return self.buyer_names