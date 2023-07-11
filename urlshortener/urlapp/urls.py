
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create/', views.create_link),
    path('<str:short_code>/', views.view_link)
]
