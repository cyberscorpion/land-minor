from django.db import models

class Land(models.Model):
    land_id = models.PositiveIntegerField()
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    land_address = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100, null = True, blank = True)
    longitude = models.CharField(max_length=100, null = True, blank = True)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

class BidLand(models.Model):
    land = models.ForeignKey(Land ,on_delete = models.CASCADE, related_name = 'lands')
    price = models.PositiveIntegerField()
    owner = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)
    itter = models.PositiveIntegerField(default = 1)
    locked = models.BooleanField(default = False)
    sell_to = models.CharField(max_length=100, null = True, blank = True)
    selling_value = models.PositiveIntegerField(null = True, blank = True)
    days = models.PositiveIntegerField(default = 30)
    token_money = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return str(self.land.land_id)

class Bid(models.Model):
    bid_land = models.ForeignKey(BidLand ,on_delete = models.CASCADE, related_name = 'bidlands')
    value = models.PositiveIntegerField()
    account = models.CharField(max_length=100)
    buyer = models.BooleanField(default = True)
    itter = models.PositiveIntegerField(default = 1)
    message = models.TextField(null = True, blank = True)
    timestamp = models.DateTimeField(auto_now=True, null=True, blank=True)
    days = models.PositiveIntegerField(default = 30)
    token_money = models.PositiveIntegerField(default = 0)
    locked = models.BooleanField(default = False)

