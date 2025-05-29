from django.urls import path
from . import views

app_name = 'businesses'

urlpatterns = [
    path('', views.business_list, name='list'),
    path('<int:pk>/', views.business_detail, name='detail'),
    path('add/', views.add_business, name='add_business'),
    path('<int:pk>/edit/', views.edit_business, name='edit_business'), 
    path('<int:pk>/delete/', views.delete_business, name='delete_business'),
    path('register/', views.register, name='register'),
]