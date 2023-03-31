from typing import Any

from django.db.models import QuerySet
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from ads.models import Ad
from ads.permissions import AdEditPermission
from ads.serializers import AdListSerializer, AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, \
    AdDeleteSerializer


class AdsListView(ListAPIView):
    """
    The Abslistview class inherits from the Listview class from the rest_framework module generics
    and is a class-based representation for processing requests by the GET method at the address '/ad/'.
    """
    queryset: QuerySet[Ad] = Ad.objects.all()
    serializer_class: ModelSerializer = AdListSerializer

    def get(self, request, *args: Any, **kwargs: Any) -> Response:
        """
        The get function overrides the method of the parent class. It is intended for processing GET requests
        at the address '/ad/'. Accepts the request object and any other positional and named parameters as arguments.
        Adds functionality to implement the display of ad search results by category, the content of the name field,
        and by price. Returns a Response object.
        """
        category_id_req: str = request.GET.get('cat', None)
        if category_id_req:
            self.queryset: QuerySet[Ad] = self.queryset.filter(
                category_id__exact=category_id_req
            )

        text_req: str = request.GET.get('text', None)
        if text_req:
            self.queryset: QuerySet[Ad] = self.queryset.filter(
                name__icontains=text_req
            )

        location_req: str = request.GET.get('location', None)
        if location_req:
            self.queryset: QuerySet[Ad] = self.queryset.filter(
                author__location__name__icontains=location_req
            )

        price_frome_req: int = request.GET.get('price_from', None)
        if price_frome_req:
            self.queryset: QuerySet[Ad] = self.queryset.filter(
                price__gte=int(price_frome_req)
            )

        price_to_req: int = request.GET.get('price_to', None)
        if price_to_req:
            self.queryset: QuerySet[Ad] = self.queryset.filter(
                price__lte=int(price_to_req)
            )

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    """
    The AdDetailView class inherits from the RetrieveAPIView class from the rest_framework generic module and is
    a class-based view for processing requests with GET methods at the address '/ad/<int: pk>'.
    The endpoint is available only to authenticated users.
    """
    queryset: QuerySet[Ad] = Ad.objects.all()
    serializer_class: ModelSerializer = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class AdCreateView(CreateAPIView):
    """
    The AdCreateView class inherits from the CreateAPIView class from the rest_framework generic module and is
    a class-based view for processing requests with POST methods at the address '/ad/create/'.
    """
    queryset: QuerySet[Ad] = Ad.objects.all()
    serializer_class: ModelSerializer = AdCreateSerializer


class AdUpdateView(UpdateAPIView):
    """
    The AdUpdateView class inherits from the UpdateAPIView class from the rest_framework generic module and is
    a class-based view for processing requests with PATCH methods at the address '/ad/<int:pk>/update/'.
    The endpoint is available only to the creator of the ad and authorized users with the role
    of administrator or moderator.
    """
    queryset: QuerySet[Ad] = Ad.objects.all()
    serializer_class: ModelSerializer = AdUpdateSerializer
    permission_classes = [AdEditPermission]


class AdDeleteView(DestroyAPIView):
    """
    The AdDeleteView class inherits from the DestroyAPIView class from the rest_framework generic module and is
    a class-based view for processing requests with DELETE methods at the address '/ad/int:pk>/delete/'.
    The endpoint is available only to the creator of the ad and authorized users with the role
    of administrator or moderator.
    """
    queryset: QuerySet[Ad] = Ad.objects.all()
    serializer_class: ModelSerializer = AdDeleteSerializer
    permission_classes = [AdEditPermission]
