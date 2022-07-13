from django.urls import path
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')


# app_name = "blog"

urlpatterns = router.urls