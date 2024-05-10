from rest_framework.routers import DefaultRouter

from app.infra.api.views import PreRegisterViewSet, ResetPassowrdViewSet, UserViewSet

router = DefaultRouter()
router.register('pre-register', PreRegisterViewSet, basename='pre-register')
router.register('users', UserViewSet, basename='users')
router.register('reset-password', ResetPassowrdViewSet, basename='reset-password')