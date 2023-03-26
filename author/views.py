from typing import Dict, Any, List

from django.db.models import QuerySet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from author.models import User, Location
from author.serializers import UserCreateSerializer, LocationSerializer, UserListSerializer, UserDetailSerializer, \
    UserDeleteSerializer, UserUpdateSerializer


class UsersListView(ListAPIView):
    """
    The UserListView class inherits from the ListView class from the django generic module and is a class-based view
    for processing requests by GET methods at the address '/user/'.
    """
    queryset = User.objects.all()
    serializer_class: ModelSerializer = UserListSerializer


class UserDetailView(RetrieveAPIView):
    """
    The UserDetailView class inherits from the DetailView class from the django generic module and is
    a class-based view for processing requests with GET methods at the address '/user/<int: pk>'.
    """
    queryset = User.objects.all()
    serializer_class: ModelSerializer = UserDetailSerializer

class UserCreateView(CreateAPIView):
    """
    The AdCreateView class inherits from the CreateView class from the django generic module and is
    a class-based view for processing requests with POST methods at the address '/user/create/'.
    """
    queryset: QuerySet[User] = User.objects.all()
    serializer_class: ModelSerializer = UserCreateSerializer


class UserUpdateView(UpdateAPIView):
    """
    The UserUpdateView class inherits from the UpdateView class from the django generic module and is
    a class-based view for processing requests with PATCH methods at the address '/user/<int:pk>/update/'.
    """
    queryset: QuerySet[User] = User.objects.all()
    serializer_class: ModelSerializer = UserUpdateSerializer


class UserDeleteView(DestroyAPIView):
    """
    The AdDeleteView class inherits from the DeleteView class of the generics module of the django base class View.
    It is intended for processing requests by the DELETE method to the url address '/user/int:pk>/delete/'.
    """
    queryset: QuerySet[User] = User.objects.all()
    serializer_class: ModelSerializer = UserDeleteSerializer


class LocationViewSet(ModelViewSet):
    """
    The LocationViewSet class inherits from the ModelViewSet class, designed to handle all requests
    defined by CRUD methods at the address '/location/'.
    """
    queryset: QuerySet[Location] = Location.objects.all()
    serializer_class: ModelSerializer = LocationSerializer
