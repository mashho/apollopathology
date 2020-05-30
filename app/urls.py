from django.urls import path, include, re_path
from . import views

urlpatterns = [

    path('', views.login, name="login"),
    path('home/', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('edit/<str:pk>/', views.edit, name="edit"),

    # path('testing/<str:pk>/',views.testing,name="testing"),
    path('create/<str:pk>/', views.submit, name="submit"),
    path('result/<str:pk>/', views.result, name="result"),
    path('about/', views.about, name="about"),

]
