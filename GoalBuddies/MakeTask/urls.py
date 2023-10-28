from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account_view, name='account'),
    path('mtask/', views.mtask_view, name='mtask'),
    path('edit_task/<int:task_id>/', views.edit_task_view, name='edit_task'),
    path('remove_task/<int:task_id>/', views.remove_task_view, name='remove_task'),
]