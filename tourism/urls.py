from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_place, name='search_place'),
    path('place/<slug:slug>/', views.place_detail, name='place_detail'),
]

