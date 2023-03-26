from django.db.models import Model
from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    The CategorySerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Category class when processing all requests
    at the address '/category/'.
    """
    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Category
        fields: str = '__all__'
