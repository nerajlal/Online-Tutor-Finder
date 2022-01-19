from django.urls import path, include
from . import views
urlpatterns = [
     path('admlogin/', views.admlogin, name="admlogin"),
     path('adm/', views.adm, name="adm"),
     path('admindex/', views.admindex, name="admindex"),
     path('Deleteuser/', views.Deleteuser, name="Deleteuser"),
      path('Deletestudent/', views.Deletestudent, name="Deletestudent"),
     path('userdelete/<int:pk>/', views.userdelete, name="userdelete"),
      path('studelete/<int:pk>/', views.studelete, name="studelete"),
   
]