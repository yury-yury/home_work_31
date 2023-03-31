from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from author.views import UserDeleteView, UserUpdateView, UserDetailView, UserCreateView, UsersListView


urlpatterns = [
    path('', UsersListView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
