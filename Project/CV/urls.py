from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Portfolio/', views.portfolio, name='portfolio'),
    path('<int:id>/', views.detailed, name='detailed'),
    path('Posts&Updates/', views.posts, name='posts'),
]
