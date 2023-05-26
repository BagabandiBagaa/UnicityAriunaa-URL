from django.db import models

# Create your models here.
TYPE_CHOICES = (
    ("Zurhnii", "Zurhnii"),
    ("Turaah", "Turaah"),
    ("Horguijuuleh", "Horguijuuleh"),
    ("Hoolbolovsruulah", "Hoolbolovsruulah"),
    ("Tolgoin", "Tolgoin"),
    ("Erchhvch", "Erchhvch"),
    ("Eregteichvvdiin", "Eregteichvvdiin"),
    ("Emegteichvvdiin", "Emegteichvvdiin"),
    ("Darhlaademjih", "Darhlaademjih"),
    ("Elegtsusnii", "Elegtsusnii"),

)
class Item(models.Model):
    def __str__(self):
        return self.item_name
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=2000)
    item_price = models.IntegerField()
    item_benefits = models.CharField(max_length=1000)
    item_image = models.CharField(max_length=2000, default="./unicity_Logo.jpg")
    item_type = models.CharField(
        max_length = 200,
        choices = TYPE_CHOICES,
        default = 'Zurhnii'
        )


class Order(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    item = models.CharField(max_length=100)
    number = models.CharField(max_length=8)
    date_ordered = models.DateTimeField(auto_now_add=True)