from typing import List

from django.db.models import Model
from rest_framework import serializers, request

from ads.models import Ad
from author.models import User
from selection.models import Selection


class SelectionListSerializer(serializers.ModelSerializer):
    """
    The SelectionListSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Selection class when processing GET requests
    at the address '/selection/'.
    """

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Selection
        fields: List[str] = ["id", "name"]


class AdForSelectionSerializer(serializers.ModelSerializer):
    """
    The Ad For Selection serializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of Ad class objects for comfortable data display when
    displaying detailed information in ad samples.
    """

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Ad
        fields: str = '__all__'


class SelectionDetailSerializer(serializers.ModelSerializer):
    """
    The SelectionDetailSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Selection class when processing GET requests
    at the address '/selection/<int: pk>/'. Overrides the value of the items field for comfortable display.
    """
    items = AdForSelectionSerializer(many=True, read_only=True)

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Selection
        fields: str = '__all__'


class SelectionCreateSerializer(serializers.ModelSerializer):
    """
    The SelectionCreateSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Selection class when processing POST requests
    at the address '/selection/create/'. Overrides the value of the id and owner fields for comfortable display.
    """
    id = serializers.IntegerField(required=False)
    owner = serializers.SlugRelatedField(
        slug_field="pk",
        queryset=User.objects.all(),
        required=False,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Selection
        fields: str = '__all__'


class SelectionUpdateSerializer(serializers.ModelSerializer):
    """
    The SelectionUpdateSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Selection class when processing PATCH requests
    at the address '/selection/<int: pk>/update/'. Overrides the value of the id field for comfortable display.
    """
    id = serializers.IntegerField(read_only=True)

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Selection
        fields: str = '__all__'


class SelectionDeleteSerializer(serializers.ModelSerializer):
    """
    The SelectionDeleteSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the Selection class when processing DELETE requests
    at the address '/selection/<int: pk>/delete/'.
    """

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Selection
        fields: List[str] = ["id"]
