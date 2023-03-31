from typing import List

from django.db import models

from ads.models import Ad
from author.models import User


class Selection(models.Model):
    """
    The Selection class is an inheritor of the Model class from the django.db.models library.
    This is the data model contained in the selection database table. Contains the description
    of the types and constraints of the fields of the base model.
    """
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        """
        The Meta class is used to change the behavior of model fields,
        such as verbose_name - a human-readable model name
        and ordering to change the order of output of model instances.
        """
        verbose_name: str = 'Пользовательская выборка объявлений'
        verbose_name_plural: str = 'Пользовательские выборки объявлений'
        ordering: List[str] = ["owner"]

    def __str__(self) -> str:
        """
        The __str__ function overrides the method of the parent class Model and creates
        an output format for instances of this class.
        """
        return self.name
