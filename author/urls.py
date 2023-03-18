from django.urls import path

from author import views


urlpatterns = [
    path('', views.UsersListView.as_view()),
    path('create/', views.UserCreateView.as_view()),
    path('<int:pk>/', views.UserDetailView.as_view()),
    path('<int:pk>/update/', views.UserUpdateView.as_view()),
    path('<int:pk>/delete/', views.UserDeleteView.as_view()),
    path('ad_by_user/', views.AdByUserDetailView.as_view()),
]
