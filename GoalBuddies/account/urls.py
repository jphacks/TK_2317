from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]