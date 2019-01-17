from django.urls import path
from .views import UserViewSet, PostViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('posts', PostViewSet, base_name='posts')
router.register('users', UserViewSet, base_name='users')
urlpatterns = router.urls
