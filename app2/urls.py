from app2.views import *
from django.urls import path

app_name='Ms_Dhoni'

urlpatterns=[
    path('temaplte1',template1,name='temaplte1'),
    path('template2/',template2,name='template2'),
]