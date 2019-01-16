from django.urls import path
from .views import UserViewSet, PostViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('posts', PostViewSet, base_name='posts')
urlpatterns = router.urls
