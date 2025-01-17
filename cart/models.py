# from django.db import models

# # Create your models here.

# from django.urls import reverse


# class Cart(models.model):
#     """Model representing a users cart"""

#     # A User can only have one Cart and a Cart can only belong to one User
#     # When the User referencing the Cart is deleted, the associated Cart will also be deleted
#     user = models.OneToOneField("User", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True, null=False)

#     def cart_total_price(self):
#         pass

#     def get_absolute_path(self):
#         """Return the URL to access a particular cart instance"""
#         return reverse("cart-detail", args=[str(self.id)])

#     def __str__(self):
#         return f"User: {self.user.id} cart"


# class CartItem(models.model):
#     """Model representing an item in a cart (an item in a cart can actually have its quantity increased by the user)"""

#     # A CartItem can have one and only one Cart (not 0 or many), but a Cart can have 0 or many CartItems
#     # When the Cart referencing the CartItem is deleted, the associated CartItem will also be deleted
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=False)

#     # A CartItem can have one and only one Product, but a Product can have 0 or many CartItems
#     product = models.ForeignKey("Product", on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     added_to_cart = models.DateTimeField(auto_now_add=True, null=False)

#     class Meta:
#         ordering = ["added_to_cart"]

#     def total_price(self):
#         # Todo: Update self.product.price according to the actual field name in Product model later
#         return self.quantity * self.product.price

#     def get_absolute_path(self):
#         return reverse("cartitem-detail", args=[str(self.id)])

#     def __str__(self):
#         # Todo: Update self.product.name according to the actual field name in product model later
#         return f"{self.quantity} x {self.product.name}"
