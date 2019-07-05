from django.contrib import admin
from django.urls import path

from .views import sp_input_view,sp_output_view

urlpatterns = [

    path('',sp_input_view),        
    path('sp_input/',sp_input_view),        
    path('sp_output/',sp_output_view),
]
