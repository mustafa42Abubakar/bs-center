from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('about/', views.about, name='about'),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
]
