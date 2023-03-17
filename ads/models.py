from django.db import models

from author.models import User
from categories.models import Category


class Ad(models.Model):
    """
    The Ads class is an inheritor of the Model class from the models library. It is a data model contained
    in the ads database table. Contains a description of the types and constraints of the model fields.
    """
    STATUS = [("TRUE", "Опубликовано"),
              ("FALSE", "Не опубликовано")]
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True)
    description = models.CharField(max_length=2000)
    is_published = models.CharField(max_length=5, choices=STATUS, default="FALSE")
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name
