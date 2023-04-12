from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from author.models import User
from categories.models import Category


class Ad(models.Model):
    """
    The Ad class is an inheritor of the Model class from the models library. It is a data model contained
    in the ads database table. Contains a description of the types and constraints of the model fields.
    """
    STATUS = [("TRUE", "Опубликовано"),
              ("FALSE", "Не опубликовано")]
    name = models.CharField(max_length=50, blank=False, null=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, validators=[MinValueValidator(0)])
    description = models.CharField(max_length=2000, blank=True, null=True)
    is_published = models.CharField(max_length=5, choices=STATUS, default="FALSE")
    image = models.ImageField(upload_to="images/")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)


    class Meta:
        """
        The Meta class is used to change the behavior of model fields,
        such as verbose_name - a human-readable model name.
        """
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self) -> str:
        """
        The __str__ function overrides the method of the parent class Model and creates
        an output format for instances of this class.
        """
        return self.name
