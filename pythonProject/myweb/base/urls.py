from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('adding/<str:id>/', views.adding, name='adding'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('login/', views.login_page, name='login'),
    path('logaut/', views.logaut_user, name='logaut'),
<<<<<<< HEAD
    path('register/', views.register_page, name='register'),
    path('delete_book/<str:id>', views.delete_clothe, name='delete_clothe'),
    path('update_user/', views.update_user, name='update_user')
=======
    path('register/', views.register_page, name='register')
>>>>>>> origin/main
]