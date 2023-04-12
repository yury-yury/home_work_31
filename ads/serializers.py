from typing import List

from django.core.exceptions import ValidationError
from django.db.models import Model
from rest_framework import serializers

from ads.models import Ad
from author.models import User
from categories.models import Category


class AdListSerializer(serializers.ModelSerializer):
    """
    The AdListSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Ad class when processing GET requests at the address '/ad/'.
    Overrides the value of the author field, for comfortable display.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username"
    )

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Ad
        fields: List[str] = ["id", "name", "price", "author"]


class AdDetailSerializer(serializers.ModelSerializer):
    """
    The AdDetailSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Ad class when processing GET requests
    at the address '/ad/<int: pk>/'. Overrides the value of the author and category fields for comfortable display.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username"
    )
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Ad
        fields: str = '__all__'


def check_status_not_TRUE(value: str):
    if value == "TRUE":
        raise ValidationError('The value of the is_published field cannot be TRUE when creating the ad.')


class AdCreateSerializer(serializers.ModelSerializer):
    """
    The AdDetailSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Ad class when processing POST requests
    at the address '/ad/create/'. Overrides the value of the author and category fields for comfortable display.
    """
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field="name"
    )
    is_published = serializers.CharField(
        max_length=5,
        default="FALSE",
        validators=[check_status_not_TRUE]
    )

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Ad
        fields: List[str] = ['id', 'name', 'description', "author", "price", "is_published", "category"]


class AdUpdateSerializer(serializers.ModelSerializer):
    """
    The AdUpdateSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Ad class when processing PATCH requests
    at the address '/ad/<int: pk>/update/'. Overrides the value of the author
    and category fields for comfortable display.
    """
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username"
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field="name"
    )

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Ad
        fields: List[str] = ["name", "price", "description", "is_published", "image", "category", "author"]


class AdDeleteSerializer(serializers.ModelSerializer):
    """
    The AdDeleteSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Ad class when processing DELETE requests
    at the address '/ad/<int: pk>/delete/'.
    """
    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Ad
        fields: List[str] = ["id"]
