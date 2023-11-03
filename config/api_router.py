from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from profi_search.users.api.views import UserViewSet

from profi_search.portfolio.urls import router as portfolio_router

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.registry.extend(portfolio_router.registry)


app_name = "api"
urlpatterns = router.urls
