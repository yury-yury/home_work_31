from django.db import models


class Category(models.Model):
    """
    The Category class is an inheritor of the Model class from the models library. It is a data model contained
    in the category table of the database. Contains a description of the types and constraints of the model fields.
    """
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

