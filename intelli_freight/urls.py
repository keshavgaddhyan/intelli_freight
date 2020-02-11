from django.conf.urls import url
from django.urls import path
from intelli_freight import views


urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report, name='report'),
    path('vessel/', views.vessel, name='vessel'),
]