from . import views
from django.urls import path,include

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('search/<str:q>/', views.PostSearch.as_view()),
    #path('<int:pk>/', views.single_post_page),
    #path('', views.index),

]