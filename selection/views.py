from typing import List

from django.db.models import QuerySet
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.serializers import ModelSerializer

from selection.models import Selection
from selection.permissions import SelectionEditPermission
from selection.serializers import SelectionListSerializer, SelectionDetailSerializer, SelectionCreateSerializer, \
    SelectionUpdateSerializer, SelectionDeleteSerializer


class SelectionListView(ListAPIView):
    """
    The Abslistview class inherits from the Listview class from the rest_framework module generics
    and is a class-based representation for processing requests by the GET method at the address '/ad/'.
    """
    queryset: QuerySet[Selection] = Selection.objects.all()
    serializer_class: ModelSerializer = SelectionListSerializer


class SelectionDetailView(RetrieveAPIView):
    """
    The AdDetailView class inherits from the RetrieveAPIView class from the rest_framework generic module and is
    a class-based view for processing requests with GET methods at the address '/ad/<int: pk>'.
    """
    queryset: QuerySet[Selection] = Selection.objects.all()
    serializer_class: ModelSerializer = SelectionDetailSerializer
    permission_classes: List[BasePermission] = [IsAuthenticated]


class SelectionCreateView(CreateAPIView):
    """
    The AdCreateView class inherits from the CreateAPIView class from the rest_framework generic module and is
    a class-based view for processing requests with POST methods at the address '/ad/create/'.
    """
    queryset: QuerySet[Selection] = Selection.objects.all()
    serializer_class: ModelSerializer = SelectionCreateSerializer
    permission_classes: List[BasePermission] = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    """
    The AdUpdateView class inherits from the UpdateAPIView class from the rest_framework generic module and is
    a class-based view for processing requests with PATCH methods at the address '/ad/<int:pk>/update/'.
    """
    queryset: QuerySet[Selection] = Selection.objects.all()
    serializer_class: ModelSerializer = SelectionUpdateSerializer
    permission_classes: List[BasePermission] = [SelectionEditPermission]


class SelectionDeleteView(DestroyAPIView):
    """
    The AdDeleteView class inherits from the DestroyAPIView class from the rest_framework generic module and is
    a class-based view for processing requests with DELETE methods at the address '/ad/int:pk>/delete/'.
    """
    queryset: QuerySet[Selection] = Selection.objects.all()
    serializer_class: ModelSerializer = SelectionDeleteSerializer
    permission_classes: List[BasePermission] = [SelectionEditPermission]
