from django.urls import path
from . import views
from .views import MenuView


app_name = 'mymenu'


urlpatterns = [
    path('', MenuView.as_view(), name="main"),
    path('<slug:item_slug>/', MenuView.as_view(), name="menu"),
    ]