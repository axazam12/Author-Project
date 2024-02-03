from . import views
from django.urls import path, include


urlpatterns=[
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),

]