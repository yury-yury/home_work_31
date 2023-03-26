from django.db.models import QuerySet
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from categories.models import Category
from categories.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """
    The CategoryViewSet class inherits from the ModelViewSet class, designed to handle all requests
    defined by CRUD methods at the address '/cat/'.
    """
    queryset: QuerySet[Category] = Category.objects.all()
    serializer_class: ModelSerializer = CategorySerializer
