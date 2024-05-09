#24-04-2024 all of this below on this date

# from django.db import models 
# from django.contrib.auth.models import User
# # Create your models here.

# class Invoice(models.Model):
#     invoice_date = models.DateField(null = True, blank = True)
#     invoice_number = models.CharField(max_length=10,null = True, blank = True)
#     name = models.CharField(max_length=100,null = True, blank = True)
#     due_date = models.DateField(null = True, blank = True)

#     # product = models.CharField(max_length=100,null = True, blank = True)
#     # qty1 = models.CharField(max_length=10,null = True, blank = True)
#     # rate1 = models.CharField(max_length=10,null = True, blank = True)
#     # total1 = models.CharField(max_length=10,null = True, blank = True)
    
#     user = models.ForeignKey(User, related_name="create_invoice",on_delete=models.DO_NOTHING)
    
#     def __str__(self):
#         return self.invoice_number


# class Product(models.Model):
#     invoice = models.ForeignKey(Invoice, related_name="product",on_delete=models.CASCADE)
#     product = models.CharField(max_length=100,null = True, blank = True)
#     qty1 = models.CharField(max_length=10,null = True, blank = True)
#     rate1 = models.CharField(max_length=10,null = True, blank = True)
#     total1 = models.CharField(max_length=10,null = True, blank = True)
    
#     def __str__(self):
#         return self.product





from django.db import models 
from django.contrib.auth.models import User
# Create your models here.

class Invoice(models.Model):
    invoice_date = models.DateField(null = True, blank = True)
    invoice_number = models.CharField(max_length=10,null = True, blank = True)
    name = models.CharField(max_length=100,null = True, blank = True)
    due_date = models.DateField(null = True, blank = True)
    product_name1 = models.CharField(max_length=100,null = True, blank = True)
    qty1 = models.CharField(max_length=10,null = True, blank = True)
    rate1 = models.CharField(max_length=10,null = True, blank = True)
    total1 = models.CharField(max_length=10,null = True, blank = True)
    user = models.ForeignKey(User, related_name="create_invoice",on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name


