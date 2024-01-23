from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, RefreshAPIView, LogoutAPIView, UpdateProfile 

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='user-registration'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
    path('refresh/', RefreshAPIView.as_view(), name='user-refresh'),
    path('logout/', LogoutAPIView.as_view(), name="user-logout"),
    path('updateprofile/', UpdateProfile.as_view(), name="update-profile"),
    ]