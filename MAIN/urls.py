from django.urls import path, include
from .import views
urlpatterns = [
     path('', views.index, name="index"),
     path('register', views.register, name="register"),
     path('register', views.register, name="register"),
     path('register_user', views.register_user, name="register_user"),
     path('login', views.login, name="login"),
     path('user_login', views.user_login, name="user_login"),
     path('about', views.about, name="about"),
     path('formView', views.formView, name="formView"),
     path('tutioninfo', views.tutioninfo, name="tutioninfo"),
    # path('admlogin', views.admlogin, name="admlogin"),
     path('studentdata', views.studentdata, name="studentdata"),
     path('tutiondata', views.tutiondata, name="tutiondata"),
     path('studentinput', views.studentinput, name="studentinput"),
     path('postdata', views.postdata, name="postdata"),
     path('uptution', views.uptution, name="uptution"),
     #    path('poststudent', views.poststudent, name="poststudent"),
     path('notification', views.notification, name="notification"),
     path('apply/<int:pk>/', views.apply, name="apply"),
      path('profile', views.profile, name="profile"),
        path('tutordata', views.tutordata, name="tutordata"),
          path('Approveuser', views.Approveuser, name="Approveuser"),
           path('approved/<int:pk>/', views.approved, name="approved")


]
