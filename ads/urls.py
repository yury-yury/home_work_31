from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from ads import views
from home_work import settings
from home_work.settings import MEDIA_ROOT


urlpatterns = [
    path('', views.AdsListView.as_view()),
    path('<int:pk>/', views.AdDetailView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
