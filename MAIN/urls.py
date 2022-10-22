from django.urls import path, include
from .import views
urlpatterns = [
     path('', views.index, name="index"),
     path('index1', views.index1, name="index1"),
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
    #  path('Approveuser', views.Approveuser, name="Approveuser"),
    # path('approved/<int:pk>/', views.approved, name="approved"),
    #   #  path('Deleteuser', views.Deleteuser, name="Deleteuser")
    # path('disapprove/<int:pk>/', views.disapprove, name="disapprove"),
    path('studentedit', views.studentedit, name="studentedit"),
    path('editstudent', views.editstudent, name="editstudent"),
    path('personalstuddata', views.personalstuddata, name="personalstuddata"),
    path('updatepersonal', views.updatepersonal, name="updatepersonal"),
    path('viewteacher/<int:pk>/', views.viewteacher, name="viewteacher"),
    path('confirmteacher/<int:pk>/', views.confirmteacher, name="confirmteacher"),
    path('personaltutordata', views.personaltutordata, name="personaltutordata"),
    path('editteacher', views.editteacher, name="editteacher"),
    path('resetpassword', views.resetpassword, name="resetpassword"),
    path('printpw', views.printpw, name="printpw"),
    path('changepwd', views.changepwd, name="changepwd"),
    path('logout',views.logout,name='logout')




]
