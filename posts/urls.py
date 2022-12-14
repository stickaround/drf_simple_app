from rest_framework.routers import DefaultRouter
from .views import PostModelViewSet

router = DefaultRouter()
router.register(r'', PostModelViewSet, basename='post')

urlpatterns = router.urls
