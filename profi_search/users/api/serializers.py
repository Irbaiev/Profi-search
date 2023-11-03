from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from profi_search.users.models import Specialist

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "url", "is_specialist", "is_employer"]
        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class CustomRegisterSerializer(RegisterSerializer):
    is_specialist = serializers.BooleanField()
    is_employer = serializers.BooleanField()

    class Meta:
        model = User
        fields = ["username", "is_specialist", "is_employer"]

    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "email": self.validated_data.get("email", ""),
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
            "is_specialist": self.validated_data.get("is_specialist", ""),
            "is_employer": self.validated_data.get("is_employer", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.is_specialist = self.cleaned_data.get("is_specialist")
        user.is_employer = self.cleaned_data.get("is_employer")
        user.save()
        adapter.save_user(request, user, self)
        return user


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['id', 'user']
