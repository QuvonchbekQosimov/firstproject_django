from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('new/<int:id>/', views.new_detail, name='new_detail'),
]
