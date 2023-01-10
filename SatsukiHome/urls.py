from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('music/', views.music, name='music'),
        path('photo/', views.photo, name='photo'),
        path('message/', views.message, name='message'),
        path('message/leave/', views.leave, name='leave'),
        path('add/' , views.add, name='add'),
        path('add/addrecord/', views.addrecord, name='addrecord'),
        ]