from django.contrib import admin
from django.urls import path, include

from .views import HomeView

from .views import HomeView, UserCreateView, UserCreateDoneView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')), # accounts/login
    path('accounts/register/', UserCreateView.as_view(), name="register"),
    path('accounts/register/done/', UserCreateDoneView.as_view(), name="register_done"),

    path('surname/', include('surname.urls')),
    path('population/', include('population.urls')),
]
