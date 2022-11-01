from . import views
from django.urls import path,include

urlpatterns = [
    path('paper/', views.paper),
    path('paper2/', views.paper2),
    path('', views.landing),
]