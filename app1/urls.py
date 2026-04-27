from django.urls import path
from . import views

urlpatterns = [
    path('',views.users_list,name='users_list'),
    path('user/<slug:slug>/', views.user_view,name='user_view'),
]
