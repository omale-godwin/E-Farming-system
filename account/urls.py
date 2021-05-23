
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login" ),
    path('register/', views.register, name="register"),
   
    path('profile/', views.profile, name="profile"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashview/', views.dashview, name="dashview"),
    path('dashcontact/', views.dashcontact, name="dashcontact"),
    path('dashpaid/', views.dashpaid, name="dashpaid"),
    path('logout/', views.logout, name="logout")
    
   
]
