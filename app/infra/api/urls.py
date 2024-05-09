from rest_framework.routers import DefaultRouter

from app.infra.api.views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')