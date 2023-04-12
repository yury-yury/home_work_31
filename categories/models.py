from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models


class Category(models.Model):
    """
    The Category class is an inheritor of the Model class from the models library. It is a data model contained
    in the category table of the database. Contains a description of the types and constraints of the model fields.
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=10, unique=True, validators=[MinLengthValidator(5), MaxLengthValidator(10)])

    class Meta:
        """
        The Meta class is used to change the behavior of model fields,
        such as verbose_name - a human-readable model name.
        """
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        """
        The __str__ function overrides the method of the parent class Model and creates
        an output format for instances of this class.
        """
        return self.name

