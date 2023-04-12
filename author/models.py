from typing import List, Tuple

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class Location(models.Model):
    """
    The Location class is an inheritor of the Model class from the models library. It is a data model contained
    in the ads database table. Contains a description of the types and constraints of the model fields.
    """
    name = models.CharField(max_length=50, default='Не указана')
    lat = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=10, decimal_places=6, null=True)

    class Meta:
        """
        The Meta class is used to change the behavior of model fields,
        such as verbose_name - a human-readable model name.
        """
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self) -> str:
        """
        The __str__ function overrides the method of the parent class Model and creates
        an output format for instances of this class.
        """
        return self.name


def validate_email(value):
    if 'rambler.ru' in value :
        raise ValidationError(
            f'{value} registration with rambler.ru prohibited ',
            params={'value': value},
        )


class User(AbstractUser):
    """
    The User class is an inheritor of the AbstractUser class from the django.contrib.auth.models library.
    This is the data model contained in the user database table. Overrides and complements the description
    of the types and constraints of the fields of the base model.
    """
    ROLE: List[Tuple[str, str]] = [('member', 'Пользователь'),
                              ('moderator', 'Модератор'),
                              ('admin', 'Администратор')]

    role = models.CharField(max_length=10, choices=ROLE, default="member")
    age = models.IntegerField(null=True)
    birth_date = models.DateField()
    email = models.EmailField(unique=True, validators=[validate_email])
    location = models.ForeignKey(Location, on_delete=models.SET_DEFAULT, default=11)

    class Meta:
        """
        The Meta class is used to change the behavior of model fields,
        such as verbose_name - a human-readable model name
        and ordering to change the order of output of model instances.
        """
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'
        ordering: List[str] = ["username"]

    def __str__(self) -> str:
        """
        The __str__ function overrides the method of the parent class Model and creates
        an output format for instances of this class.
        """
        return self.username
