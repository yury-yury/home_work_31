from typing import List

from django.db.models import Model
from rest_framework import serializers

from author.models import User, Location


class UserListSerializer(serializers.ModelSerializer):
    """
    The UserListSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the User class when processing GET requests
    at the address '/user/'. Overrides the value of the location field for comfortable display.
    """
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name",
    )

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = User
        fields: List[str] = ["id", "username", "first_name", "last_name", "role", "age", "location"]


class UserDetailSerializer(serializers.ModelSerializer):
    """
    The UserDetailSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the User class when processing GET requests
    at the address '/user/<int: pk>/'. Overrides the value of the location field, for a comfortable display.
    """
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field="name"
    )

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = User
        fields: str = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    """
    The UserCreateSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the User class when processing POST requests
    at the address '/user/create/'. Overrides the value of the location field, for a comfortable display.
    """
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = User
        fields: str = '__all__'

    def is_valid(self, *, raise_exception=False):
        """
        The is_valid function overrides the method of the parent class. Accepts the request object
        and any positional and named arguments as arguments. Adds functionality for converting incoming data
        to a format supported by the model. Returns the method of the parent class.
        """
        if "location" in self.initial_data:
            self._location = self.initial_data.pop("location")
            if type(self._location) == list:
                self._location = ", ".join(self._location)
            location_object, _ = Location.objects.get_or_create(name=self._location)
            self.initial_data["location"] = self._location
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """
    The UserUpdateSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the User class when processing PATCH requests
    at the address '/user/<int: pk/update/'. Overrides the value of the location field, for a comfortable display.
    """
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field="name"
    )
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = User
        fields: str = '__all__'

    def is_valid(self, *, raise_exception=False):
        """
        The is_valid function overrides the method of the parent class. Accepts the request object
        and any positional and named arguments as arguments. Adds functionality for converting incoming data
        to a format supported by the model. Returns the method of the parent class.
        """
        if "location" in self.initial_data:
            self._location = self.initial_data.pop("location")
            if type(self._location) == list:
                self._location = ", ".join(self._location)
            location_object, _ = Location.objects.get_or_create(name=self._location)
            self.initial_data["location"] = self._location
        return super().is_valid(raise_exception=raise_exception)


class UserDeleteSerializer(serializers.ModelSerializer):
    """
    The UserDeleteSerializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of Ad class objects when processing DELETE requests
    at the address '/user/<int: pk>/delete/'.
    """
    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = User
        fields: List[str] = ["id"]


class LocationSerializer(serializers.ModelSerializer):
    """
    The Location Serializer class inherits from the serializer class.ModelSerializer is a class for convenient
    serialization and deserialization of objects of the User class when processing all requests
    at the address '/location/'.
    """
    class Meta:
        """
        The Meta class is an internal service class of the serializer,
        defines the necessary parameters for the serializer to function.
        """
        model: Model = Location
        fields: str = '__all__'
