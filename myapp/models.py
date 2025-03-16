from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()  # Add this field

    def __str__(self):
        return self.name


