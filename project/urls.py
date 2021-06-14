from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListProject.as_view()),
    path('<int:pk>/', views.DetailProject.as_view()),
]
