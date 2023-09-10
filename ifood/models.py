from django.db import models


class Suggestion(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=255)


class Promotion(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=255)


class Offer(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.CharField(max_length=255)
    delivery = models.CharField(max_length=255)
    delay = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Restaurant(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    star = models.DecimalField(max_digits=2, decimal_places=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    delay = models.CharField(max_length=255)
    distance = models.CharField(max_length=255)
