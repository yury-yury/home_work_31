import json
from typing import Dict, List, Any

from django.db import models
from django.http import JsonResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from categories.models import Category


class CategoriesListView(ListView):
    """
    The CategoriesListView class inherits from the ListView class from the django generic module and
    is a class-based view for processing requests by GET method at the address '/cat/'.
    """
    model: models.Model = Category

    def get(self,request, *args, **kwargs) -> JsonResponse:
        """
        The get function is a class-based view method for processing a GET request at the address '/cat/'.
        Takes a request object as an argument. Makes a query from the database of all values and returns
        the result in the form of JSON.
        """
        super().get(request, *args, **kwargs)
        categories = self.object_list
        categories = categories.order_by("name")
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)


class CategoryDetailView(DetailView):
    """
    The CategoryDetailView class inherits from the DetailView class from the django generic module and is
    a class-based view for processing requests with GET methods at the address '/cat/<int: pk>'.
    """
    model: models.Model = Category
    def get(self, request, *args, **kwargs) -> JsonResponse:
        """
        The get function is a class-detail view method for processing a GET request at the address '/cat/<int:pk>'.
        Designed to get detailed data about the requested object. Takes a request object as an argument.
        Returns the result as JSON.
        """
        category: Category = self.get_object()
        response: Dict[str, str] = {
            "id": category.id,
            "name": category.name
        }
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    """
    The CategoryCreateView class inherits from the CreateView class from the django generic module and is
    a class-based view for processing requests with POST methods at the address '/cat/create/'.
    """
    model: models.Model = Category
    fields: List[str] = ['name',]

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """
        The post function is a class-based view method for processing a POST request at the address '/cat/create'.
        Designed to add a new object to the database. Takes a request object as an argument.
        Retrieves the data of a new object from the request body, generates and stores the object in the database.
        Returns the saved object as JSON.
        """
        category_data = json.loads(request.body)

        category: Category = Category.objects.create(name=category_data['name'])

        response: Dict[str, Any] = {
                "id": category.id,
                "name": category.name
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    """
    The CategoryUpdateView class inherits from the UpdateView class from the django generic module and is
    a class-based view for processing requests with PATCH methods at the address '/cat/<int:pk>/update/'.
    """
    model: models.Model = Category
    fields: List[str] = ['name',]

    def patch(self, request, *args, **kwargs):
        """
        The patch function is a class-based view method for processing a PATCH request
        at the address '/cat/<int:pk>/update/'. Designed to update the object to the database. Takes a request object
        as an argument. Retrieves the data for update of the object from the request body, updates and stores
        the object in the database. Returns the saved object as JSON.
        """
        super().get(request, *args, **kwargs)

        category_data = json.loads(request.body)

        self.object.name = category_data['name']

        self.object.save()

        response: Dict[str, Any] = {
            "id": self.object.id,
            "name": self.object.name,
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    """
    The CategoryDeleteView class inherits from the DeleteView class of the generics module of the django base class View.
    It is intended for processing requests by the DELETE method to the url address '/cat/int:pk>/delete/'.
    """
    model: models.Model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs) -> JsonResponse:
        """
        The delete function overrides the method of the AdDeleteView class. Accepts a request object as parameters
        and can accept other positional and named arguments. Deletes the requested object from the database.
        Returns a message in JSON format.
        """
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "OK"}, status=200)
