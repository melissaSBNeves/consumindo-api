from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_year, name='form-holiday' ),
    path('form/', views.get_holiday, name='get-holiday-by-year'),
    path('save/', views.save_holiday, name='create-holiday'),
    path('list/', views.holiday_list, name='list-holiday'),
    path('delete/<int:pk>', views.holiday_delete, name='delete-holiday')
]