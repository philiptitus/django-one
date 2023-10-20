from django.urls import path
from .  import views


app_name = 'todo_app'

urlpatterns = [

    path('register/', views.register,name='register'),
    path('login/',views.u_login,name='login'),
    path('task/',views.to_do,name='task'),
    path('view_task',views.records,name='view_task'),

]
