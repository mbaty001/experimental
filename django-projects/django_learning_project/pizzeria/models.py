from django.db import models

class Pizza(models.Model):
    name = models.TextField(max_length=30)

    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.TextField(max_length=20)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)