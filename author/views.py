import json
from typing import Dict, Any, List
from django.core.paginator import Paginator
from django.db import models
from django.db.models import Count
from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from author.models import User, Location
from home_work import settings


class UsersListView(ListView):
    """
    The UserListView class inherits from the ListView class from the django generic module and is a class-based view
    for processing requests by GET methods at the address '/user/'.
    """
    model: models.Model = User

    def get(self,request, *args, **kwargs) -> JsonResponse:
        """
        The get function is a class-based view method for processing a GET request at the address '/user/'.
        Takes a request object as an argument. Makes a query from the database of all values and returns
        the result in the form of JSON.
        """
        super().get(request, *args, **kwargs)

        users = self.object_list

        response: list = []
        for user in users:
            response.append({
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "age": user.age,
                "locations": Location.objects.get(pk=user.location_id).name
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False}, status=200)


class UserDetailView(DetailView):
    """
    The UserDetailView class inherits from the DetailView class from the django generic module and is
    a class-based view for processing requests with GET methods at the address '/user/<int: pk>'.
    """
    model: models.Model = User

    def get(self, request, *args, **kwargs) -> JsonResponse:
        """
        The get function is a class-detail view method for processing a GET request at the address '/user/<int:pk>'.
        Designed to get detailed data about the requested object. Takes a request object as an argument.
        Returns the result as JSON.
        """
        user: User = self.get_object()
        response: Dict[str, Any] = {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "locations": Location.objects.get(pk=user.location_id).name.split(', ')
        }
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False}, status=200)


class AdByUserDetailView(View):
    """
    The AdByUserDetailView class inherits from the View class from the django module and is
    a class-based view for processing requests with GET methods at the address '/user/ad_by_user/'.
    """
    def get(self, request) -> JsonResponse:
        """
        The get function overrides the method of the AdByUserDetailView class. Processes requests
        by the GET method according to the GC '/user/ad_by_user/'/ Accepts the request object and other positional
        and named arguments as parameters. Requests database records.
        Adds a grouping field. Returns the result in JSON format.
        """
        user_query_set = User.objects.annotate(total_ads=Count('ad'))

        paginator: Paginator = Paginator(user_query_set, settings.TOTAL_ON_PAGE)
        page_number: int = int(request.GET.get("page", 1))
        page_object = paginator.get_page(page_number)

        users: list = []
        for user in page_object:
            users.append({
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "age": user.age,
                "location": Location.objects.get(pk=user.location_id).name.split(', '),
                "total_ads": user.total_ads,
            })

        response: Dict[str, Any] = {
            "items": users,
            "total": paginator.count,
            "num_page": paginator.num_pages
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    """
    The AdCreateView class inherits from the CreateView class from the django generic module and is
    a class-based view for processing requests with POST methods at the address '/user/create/'.
    """
    model: models.Model = User
    fields: List[str] = ["first_name", "last_name", "username", "password", "role", "age", "location"]

    def post(self, request, *args, **kwargs) -> JsonResponse:
        """
        The post function is a class-based view method for processing a POST request at the address '/cat/create/'.
        Designed to add a new object to the database. Takes a request object as an argument.
        Retrieves the data of a new object from the request body, generates and stores the object in the database.
        Returns the saved object as JSON.
        """
        user_data = json.loads(request.body)

        if type(user_data['locations']) == list:
            user_data['locations'] = ', '.join(user_data['locations'])
        try:
            location: Location = Location.objects.get(name=user_data['locations'])
        except Location.DoesNotExist:
            location: Location = Location.objects.create(name=user_data['locations'])
            location.save()

        user = User.objects.create(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            username=user_data['username'],
            password=user_data['password'],
            role=user_data['role'],
            age=user_data['age'],
            location_id=location.id)

        response: Dict[str,Any] = {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "locations": location.name.split(', ')
}
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    """
    The UserUpdateView class inherits from the UpdateView class from the django generic module and is
    a class-based view for processing requests with PATCH methods at the address '/user/<int:pk>/update/'.
    """
    model: models.Model = User
    fields: List[str] = ["first_name", "last_name", "username", "password", "role", "age", "location"]

    def patch(self, request, *args, **kwargs) -> JsonResponse:
        """
        The patch function is a class-based view method for processing a PATCH request
        at the address '/user/<int:pk>/update/'. Designed to update the object to the database. Takes a request object
        as an argument. Retrieves the data for update of the object from the request body, updates and stores
        the object in the database. Returns the saved object as JSON.
        """
        super().get(request, *args, **kwargs)

        user_data = json.loads(request.body)

        if type(user_data['locations']) == list:
            user_data['locations'] = ', '.join(user_data['locations'])
        try:
            location: Location = Location.objects.get(name=user_data['locations'])
        except Location.DoesNotExist:
            location: Location = Location.objects.create(name=user_data['locations'])
            location.save()

        self.object.username = user_data["username"]
        self.object.password = user_data["password"]
        self.object.first_name = user_data["first_name"]
        self.object.last_name = user_data["last_name"]
        self.object.age = user_data["age"]
        self.object.locations = location.id

        self.object.save()

        response: Dict[str, Any] = {
            "id": self.object.id,
            "username": self.object.username,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "age": self.object.age,
            "locations": location.name.split(', ')
        }

        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    """
    The AdDeleteView class inherits from the DeleteView class of the generics module of the django base class View.
    It is intended for processing requests by the DELETE method to the url address '/user/int:pk>/delete/'.
    """
    model: models.Model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs) -> JsonResponse:
        """
        The delete function overrides the method of the AdDeleteView class. Accepts a request object as parameters
        and can accept other positional and named arguments. Deletes the requested object from the database.
        Returns a message in JSON format.
        """
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "OK"}, status=200)
