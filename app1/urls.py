from app1.views import *
from django.urls import path

app_name='virat kohli'

urlpatterns=[
    path('template1/',template1,name='template1'),
    path('template2/',template2,name='template2'),
    
]