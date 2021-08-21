from django.urls import path
from users import views
urlpatterns = [
    path('', views.home, name = "home"),
    #path('')
    path('register/', views.register, name = "register"),
    path('login/', views.login_view, name = "login"),
    path('logout/login', views.logout_view, name = "logout"),

]