from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_routes),
    path('clothes/', views.get_clothes),
    path('clothes/<str:id>', views.get_clothe)
    ]
