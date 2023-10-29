from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account_view, name='account'),
    path('mtask/', views.mtask_view, name='mtask'),
    path('edit_task/<int:task_id>/', views.edit_task_view, name='edit_task'),
    path('remove_task/<int:task_id>/', views.remove_task_view, name='remove_task'),
    path('match_task/<int:task_id>/', views.match_task_view, name='match_task'),
    path('task_detail/<int:task_id>/', views.task_detail_view, name='task_detail'),
]