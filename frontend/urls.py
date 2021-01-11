from django.urls import path
from . import views

app_name = 'front'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.index, name='index'),
]