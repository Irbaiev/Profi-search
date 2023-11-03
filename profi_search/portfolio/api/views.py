from rest_framework import viewsets

from profi_search.portfolio.models import Education, Service, WorkExperience, Speciality, Portfolio
from profi_search.portfolio.api.serializers import (
    EducationSerializer,
    WorkExperienceSerializer,
    ServiceSerializer,
    SpecialitySerializer,
    PortfolioSerializer,
)

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.select_related("specialist")
    serializer_class = EducationSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.select_related("specialist")
    serializer_class = ServiceSerializer


class WorkExperienceViewSet(viewsets.ModelViewSet):
    queryset = WorkExperience.objects.select_related('specialist')
    serializer_class = WorkExperienceSerializer


class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.select_related('specialist')
    serializer_class = SpecialitySerializer

    
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.select_related("specialist")
    serializer_class = PortfolioSerializer
