from django.contrib import admin
from django.urls import path

from .views import sp_input_view,sp_output_view
from .views2 import api_view,api_doc_view

urlpatterns = [

    path('',sp_input_view),        
    path('sp_input/',sp_input_view),        
    path('sp_output/',sp_output_view),
    path('api_doc',api_doc_view),
    path('api',api_view),
]
