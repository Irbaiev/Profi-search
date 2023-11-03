from rest_framework import serializers

from profi_search.portfolio.models import Education, WorkExperience, Service, Speciality, Portfolio
from profi_search.users.api.serializers import SpecialistSerializer


class EducationSerializer(serializers.ModelSerializer):
    specialist = SpecialistSerializer()

    class Meta:
        model = Education
        fields = [
            "id",
            "name",
            "faculty",
            "specialization",
            "start_at",
            "end_at",
            "specialist",
        ]


class ServiceSerializer(serializers.ModelSerializer):
    specialist = SpecialistSerializer()

    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "price",
            "specialist",
        ]
        fields = ["id",
                  "name",
                  "faculty",
                  "specialization",
                  "start_at",
                  "end_at",
                  "specialist",]

class WorkExperienceSerializer(serializers.ModelSerializer):
    specialist = SpecialistSerializer()

    class Meta:
        model = WorkExperience
        fields = ["id",
                  "specialist",
                  "title",
                  "description",
                  "start_at",
                  "end_at",
                  "organization",
                  "city",
                  "position"]

class SpecialitySerializer(serializers.ModelSerializer):
    specialist = SpecialistSerializer()

    class Meta:
        model = Speciality
        fields = [
                    "id",
                    "specialist",
                    "title", ]
class PortfolioSerializer(serializers.ModelSerializer):
    specialist = SpecialistSerializer()

    class Meta:
        model = Portfolio
        fields = ["id",
                  "specialist",
                  "title",
                  "image",
                  "description",
                  "start_at",
                  "end_at",
                  "organization"]
