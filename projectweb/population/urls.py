from django.contrib import admin
from django.urls import path, include

from .views import HomeView, SearchPastView, SearchFutureView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    
    path('search/<str:key>', SearchPastView.as_view(), name="search"),
    path('search/future/<str:key>', SearchFutureView.as_view(), name="future"),
]