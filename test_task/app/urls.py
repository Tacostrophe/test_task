from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('task_1/', views.task_1_view, name="task_1"),
    path('task_2/', views.task_2_view, name="task_2")
]
