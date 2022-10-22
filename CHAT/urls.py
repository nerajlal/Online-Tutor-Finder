from django.urls import path, include
from . import views
urlpatterns = [
     path('index/<int:pk>/', views.index, name="index"),
     path('index2/', views.index2, name="index2"),
      path('index3/', views.index3, name="index3"),
      path('msg/', views.msg, name="msg"),
      path('msg2/', views.msg2, name="msg2"),
      path('chatNotification/', views.chatNotification, name="chatNotification"),
      path('chatFromnotification/<int:pk>/', views.chatFromnotification, name="chatFromnotification"),
      path('index4/', views.index4, name="index4"),
    #  path('chat/', views.chat, name="chat"),
]