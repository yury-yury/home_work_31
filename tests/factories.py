import factory.django

from author.models import User
from ads.models import Ad
from categories.models import Category


class UserFactory(factory.django.DjangoModelFactory):
    """
    The UserFactory class is a factory for creating test instances corresponding to the User model in order
    to verify the correct functioning of the application.
    """
    username: str = factory.Faker("user_name")
    password: str = "1234"
    email: str = factory.Faker("email")

    class Meta:
        """
        The Meta class contains an indication of the model for creating test instances of objects that replace
        data from the database.
        """
        model = User


class CategoryFactory(factory.django.DjangoModelFactory):
    """
    The CategoryFactory class is a factory for creating test instances corresponding to the Category model
    in order to verify the correct functioning of the application.
    """
    name: str = factory.Faker("user_name")
    slug: str = factory.Faker("text", max_nb_chars=10)

    class Meta:
        """
        The Meta class contains an indication of the model for creating test instances of objects that replace
        data from the database.
        """
        model = Category


class AdFactory(factory.django.DjangoModelFactory):
    """
    The AdFactory class is a factory for creating test instances corresponding to the Ad model in order to verify
    the correct functioning of the application.
    """
    name: str = "test name 1"
    description: str = "test text"
    price: int = 100
    author: User = factory.SubFactory(UserFactory)
    category: Category =factory.SubFactory(CategoryFactory)

    class Meta:
        """
        The Meta class contains an indication of the model for creating test instances of objects that replace
        data from the database.
        """
        model = Ad
