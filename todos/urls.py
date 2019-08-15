from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add, name='add'),
    path('my_details/', views.my_details, name='my_details'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('complete/<list_id>', views.complete, name='complete'),
]