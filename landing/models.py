from django.db import models


class Dron(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.price} $'
    
    
    
# add date and country also not forget to make migrations and migrate
# create registration view and template