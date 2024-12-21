from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from django.urls import path, include
from .views import UserRegisterView, UserDetailView

urlpatterns = [
    path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("token/logout/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path('users/register/', UserRegisterView.as_view(), name='user_register_view'),
    path('users/me/', UserDetailView.as_view(), name='me_view')
]
