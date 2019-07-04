from django.db import models

prod_category = (
    (1, "Men's Clothing"),
    (2, "Women's Clothing"),
    (3, "Electronic's"),
    (4, "Furniture"),
    (5, "Books"),
    (6, "Others"),
)


class Login(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=50)


class Signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class add_prod_for_rent(models.Model):
    p_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=prod_category, default='Others')
    short_description = models.TextField(blank=True, null=True)
    rent_price = models.DecimalField(decimal_places=2, max_digits=10)
    prod_age = models.IntegerField()

    def __str__(self):
        return self.prod_name


class add_prod_for_sell(models.Model):
    p_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=prod_category, default='Others')
    short_description = models.TextField(blank=True, null=True)
    sell_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.prod_name


class RentFeedback(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    p_id = models.ForeignKey(add_prod_for_rent, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)


class SellFeedback(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    p_id = models.ForeignKey(add_prod_for_sell, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True)
