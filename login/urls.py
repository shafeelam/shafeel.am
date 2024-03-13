from django.urls import path
from . import views

urlpatterns = [
     path('register',views.register, name='register'),
     path('login',views.login,name='login'),
     path('messages',views.messages,name='messages'),
     path('logout',views.logout,name='logout')
]
     