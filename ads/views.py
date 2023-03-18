import json
from typing import List, Dict, Union, Any

from django.core.paginator import Paginator
from django.db import models
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Ad
from author.models import User
from home_work import settings


class AdsListView(ListView):
    """
    The AdsListView class inherits from the ListView class from the django.generic module and is a class-based view
    for processing requests by GET method at the address '/ad/'.
    """
    model:models.Model = Ad

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """
        The get function is a class-based view method for processing a GET request at the address '/ad/'.
        Takes a request object as an argument. Makes a query from the database of all values and returns
        the result in the form of JSON.
        """
        super().get(request, *args, **kwargs)
        ads = self.object_list
        ads = ads.order_by("-price")

        paginator: Paginator = Paginator(ads, settings.TOTAL_ON_PAGE)
        page_number: int = int(request.GET.get("page", 1))
        page_object: List[Ad] = paginator.get_page(page_number)

        ads_list: list = []
        for ad in page_object:
            ads_list.append({
                "id": ad.id,
                "name": ad.name,
                "price": ad.price,
                "user": ad.author_id
            })

            response: Dict = {
                "items": ads_list,
                "num_pages": paginator.num_pages,
                "total": paginator.count
            }

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)


class AdDetailView(DetailView):
    """
    The AdDetailView class inherits from the DetailView class from the django generic module and is
    a class-based view for processing requests with GET methods at the address '/ad/<int: pk>'.
    """
    model:models.Model = Ad

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """
        The get function is a class-detail view method for processing a GET request at the address '/ad/<int:pk>'.
        Designed to get detailed data about the requested object. Takes a request object as an argument.
        Returns the result as JSON.
        """
        ad: Ad = self.get_object()

        response = {"id": ad.id,
                    "name": ad.name,
                    "user_id": ad.author_id,
                    "user": User.objects.get(pk=ad.author_id).username,
                    "price": int(ad.price),
                    "description": ad.description,
                    "is_published": ad.is_published,
                    "category": ad.category_id,
                    "image": ad.image.url if ad.image else None}

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    """
    The AdCreateView class inherits from the CreateView class from the django generic module and is
    a class-based view for processing requests with POST methods at the address '/ad/create/'.
    """
    model:models.Model = Ad
    fields: List[str] = ["name", "author_id", "price", "description", "is_published", "image", "category_id"]

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """
        The post function is a class-based view method for processing a POST request at the address '/ad/create/'.
        Designed to add a new object to the database. Takes a request object as an argument.
        Retrieves the data of a new object from the request body, generates and stores the object in the database.
        Returns the saved object as JSON.
        """
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data["name"],
            price=int(ad_data["price"]),
            description=ad_data["description"],
            author_id=int(ad_data["user"]),
            category_id=int(ad_data["category"])
        )

        response = {
            "id": ad.id,
            "name": ad.name,
            "user": ad.author_id,
            "description": ad.description,
            "is_published": ad.is_published,
            "price": ad.price
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    """
    The AdUpdateView class inherits from the UpdateView class from the django generic module and is
    a class-based view for processing requests with PATCH methods at the address '/ad/<int:pk>/update/'.
    """
    model:models.Model = Ad
    fields: List[str] = ["name", "price", "description", "is_published", "image", "category"]

    def patch(self, request, *args, **kwargs) -> JsonResponse:
        """
        The patch function is a class-based view method for processing a PATCH request
        at the address '/ad/<int:pk>/update/'. Designed to update the object to the database. Takes a request object
        as an argument. Retrieves the data for update of the object from the request body, updates and stores
        the object in the database. Returns the saved object as JSON.
        """
        super().get(request, *args, **kwargs)

        ad_data = json.loads(request.body)

        self.object.name = ad_data['name']
        self.object.price = int(ad_data["price"])
        self.object.description = ad_data["description"]
        self.object.category_id = int(ad_data["category"])

        self.object.save()

        response = {"id": self.object.id,
                    "name": self.object.name,
                    "user": self.object.author_id,
                    "price": int(self.object.price),
                    "description": self.object.description,
                    "is_published": self.object.is_published,
                    "category": self.object.category_id}

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    """
    The AdImageView class inherits from the UpdateView class of the generics module of the django base class View.
    It is intended for processing requests by the POST method to the url address '/ad/int:pk>/upload_image/'.
    """
    model:models.Model = Ad
    fields: List[str] = ["name", "price", "description", "is_published", "image", "category", "author"]

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """
        The post function overrides the method of the AdImageView class. Accepts a request object as parameters
        and can accept other positional and named arguments. Updates the 'image' field in an existing ad with
        the addition of the uploaded image. Returns updated data of the requested ad in JSON format.
        """
        self.object = self.get_object()

        self.object.image = request.FILES["image"]

        self.object.save()

        response: Dict[str, Any] = {
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": User.objects.get(pk=self.object.author_id).username,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "image": self.object.image.url if self.object.image else None
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    """
    The AdDeleteView class inherits from the DeleteView class of the generics module of the django base class View.
    It is intended for processing requests by the DELETE method to the url address '/ad/int:pk>/delete/'.
    """
    model:models.Model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs) -> JsonResponse:
        """
        The delete function overrides the method of the AdDeleteView class. Accepts a request object as parameters
        and can accept other positional and named arguments. Deletes the requested object from the database.
        Returns a message in JSON format.
        """
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "OK"}, status=200)
