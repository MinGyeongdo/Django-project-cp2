from django.urls import path
from . import views

urlpatterns=[ 
path('userdatas/', views.getTestDatas, name='userdatas'),
]