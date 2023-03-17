import json

from django.http import JsonResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.decorators import method_decorator

from categories.models import Category


class CategoriesListView(ListView):
    """
    The CategoriesView class inherits from the View class from the django module and is a class-based view
    for processing requests by GET and POST methods at the address '/cat/'.
    """
    model = Category

    def get(self,request, *args, **kwargs) -> JsonResponse:
        """
        The get function is a class-based view method for processing a GET request at the address '/cat/'.
        Takes a request object as an argument. Makes a query from the database of all values and returns
        the result in the form of JSON.
        """
        super().get(request, *args, **kwargs)
        categories = self.object_list
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class CategoryDetailView(DetailView):
    """
    The CategoryDetailView class inherits from the DetailView class from the django generic module and is
    a class-based view for processing requests with GET methods at the address '/cat/<int: pk>'.
    """
    model = Category
    def get(self, request, *args, **kwargs) -> JsonResponse:
        """
        The get function is a class-detail view method for processing a GET request at the address '/cat/<int:pk>'.
        Designed to get detailed data about the requested object. Takes a request object as an argument.
        Returns the result as JSON.
        """
        category = self.get_object()
        response = {"id": category.id, "name": category.name}
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    """

    """
    model = Category
    fields = ['name',]

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """
        The post function is a class-based view method for processing a POST request at the address '/cat/'.
        Designed to add a new object to the database. Takes a request object as an argument.
        Retrieves the data of a new object from the request body, generates and stores the object in the database.
        Returns the saved object as JSON.
        """
        category_data = json.loads(request.body)

        category = Category.objects.create(name=category_data['name'])


        response = {
                "id": category.id,
                "name": category.name
        }
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name',]

    def patch(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        category_data = json.loads(request.body)

        self.object.name = category_data['name']

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "OK"}, status=200)
