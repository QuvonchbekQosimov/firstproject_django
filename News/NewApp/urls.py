from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('page/', views.page, name='page'),
    path('news/', views.news, name='news'),
    path('new_detail/<int:id>/', views.new_detail, name='new_detail'),
]
