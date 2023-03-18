from django.db import models


class Location(models.Model):
    """
    The Location class is an inheritor of the Model class from the models library. It is a data model contained
    in the ads database table. Contains a description of the types and constraints of the model fields.
    """
    name = models.CharField(max_length=50)
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


class User(models.Model):
    """
    The User class is an inheritor of the Model class from the models library. It is a data model contained
    in the ads database table. Contains a description of the types and constraints of the model fields.
    """
    ROLE = [('member', 'Пользователь'),
            ('moderator', 'Модеоатор'),
            ('admin', 'Администратор')]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=ROLE, default="member")
    age = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        """
        The Meta class is used to change the behavior of model fields,
        such as verbose_name - a human-readable model name
        and ordering to change the order of output of model instances.
        """
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["username"]

    def __str__(self) -> str:
        """
        The __str__ function overrides the method of the parent class Model and creates
        an output format for instances of this class.
        """
        return self.username
