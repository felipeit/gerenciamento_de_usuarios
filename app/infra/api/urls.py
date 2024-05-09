from rest_framework.routers import DefaultRouter

from app.infra.api.views import ResetPassowrdViewSet, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('reset-password', ResetPassowrdViewSet, basename='reset-password')