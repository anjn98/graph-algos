"""spfa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

from spfa1.views import sp_input_view,sp_output_view,home_view, projects_view, profiles_view, resume_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),


    path('projects/',projects_view),
    path('profiles/',profiles_view),
    path('resume/',resume_view),

    path('sp_input/',sp_input_view),


    
    path('sp_output/',sp_output_view),
]
