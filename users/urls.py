from django.urls import path
from .views import RegisterView, UserListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('list/', UserListView.as_view(), name='user-list'),
    
    # Path to login and get the token
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Path to get a new access token using the refresh token
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]