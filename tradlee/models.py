from django.db import models

prod_category = (
    ("Men's Clothing"),
    ("Women's Clothing"),
    ("Electronic's"),
    ("Furniture"),
    ("Books"),
    ("Others"),
)
ad_category = (
    ('sell',"Sell"),
    ('rent',"Rent"),
    ('both',"Both"),
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

class Product(models.Model):
    prod_name = models.CharField(max_length=255)
    category = models.CharField(max_length=50 , choices=prod_category , default='Others')
    short_description = models.TextField(blank=True, null=True)
    for_what = models.CharField(max_length=10 , choices=ad_category , default='Sell')
    rent_price = models.DecimalField(decimal_places=2,max_digits=10)
    sell_price = models.DecimalField(decimal_places=2, max_digits=10)
    prod_age = models.IntegerField(max_length=2)

class Feedback(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    product = models.ForeignKey(Product)
    message = models.TextField(blank=True , null=True)


