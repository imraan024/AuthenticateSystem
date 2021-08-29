from django.urls import path
from users import views
urlpatterns = [
    path('', views.home, name = "user-info"),
    path('register/', views.register, name = "register"),
    path('login/', views.login_view, name = "login"),
    path('logout', views.logout_view, name = "logout"),
    path('edit_profile', views.EditProfile, name= "edit"),
    path('verified/<auth_token>', views.verifiedView, name = "verified"),
    path('send_mail/', views.sendEmailView, name = "send-email"),
    path('error' , views.errorPage , name="error")

]