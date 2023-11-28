from django.contrib import admin 
from django.urls import path, include 
from django.conf.urls import url 
from core.views import *
  
urlpatterns = [ 
    # path('admin/', admin.site.urls), 
    path('login/', loginView.as_view(), name="something"), 
    path('signup/', signupView.as_view(), name="somethingelse"),  
]