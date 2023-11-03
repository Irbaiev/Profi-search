from rest_framework import routers

from profi_search.portfolio.api.views import EducationViewSet, WorkExperienceViewSet, ServiceViewSet, SpecialityViewSet, PortfolioViewSet 

app_name = "portfolio"

router = routers.SimpleRouter()
router.register("education", EducationViewSet, basename="education")
router.register("service", ServiceViewSet, basename="service")
router.register("workexperience", WorkExperienceViewSet, basename='workexperience')
router.register("speciality", SpecialityViewSet, basename="speciality")
router.register("portfolio",PortfolioViewSet, basename='portfolio')
urlpatterns = router.urls
