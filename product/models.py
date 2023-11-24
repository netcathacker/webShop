from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
