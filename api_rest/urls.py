
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('user/<int:id>', views.get_by_id, name='get-user-by-id' ),

]
 