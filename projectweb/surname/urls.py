from django.contrib import admin
from django.urls import path, include

from .views import HomeView, SearchView, SearchDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('search/<str:key>', SearchView.as_view(), name="search"),
    path('detail/<str:key>', SearchDetailView.as_view(), name="detail"),
]