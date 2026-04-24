from django.urls import path
from . import views

urlpatterns = [
    path('',views.users_list,name='users_list'),
    path('users/<int:user_id>/', views.user_view,name='user_view'),
]
