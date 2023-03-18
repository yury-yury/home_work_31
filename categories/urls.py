from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from categories import views
from home_work import settings
from home_work.settings import MEDIA_ROOT


urlpatterns = [
    path('', views.CategoriesListView.as_view()),
    path('create/', views.CategoryCreateView.as_view()),
    path('<int:pk>/', views.CategoryDetailView.as_view()),
    path('<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('<int:pk>/delete/', views.CategoryDeleteView.as_view()),
]

