from django.urls import path
from .views import UserCreateView, LoginView, UserIsAuthenticated, ChangePassword, ProfileUpdateView
from knox import views as knox_views

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
	path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('checkauth/', UserIsAuthenticated.as_view()),
    path('updatepassword/', ChangePassword.as_view()),
    path('updateprofile/', ProfileUpdateView.as_view()),
]