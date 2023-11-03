from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """
    Default custom user model for Profi Search
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    middle_name = models.CharField("Отчество", null=True, blank=True, max_length=32)
    about = models.TextField("О себе", null=True, blank=True)
    city = models.CharField("Город", null=True, blank=True, max_length=32)
    avatar = models.ImageField("Аватар", upload_to="user_avatars/", null=True)
    is_specialist = models.BooleanField("Специалист", default=False)
    is_employer = models.BooleanField("Работодатель", default=False)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Specialist(models.Model):
    class Gender(models.TextChoices):
        WOMAN = "WM", _("Женщина")
        MAN = "M", _("Мужчина")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField("Возраст", null=True, blank=True)
    gender = models.CharField(
        "Пол", null=True, blank=True, choices=Gender.choices, max_length=7
    )
    phone = PhoneNumberField("Телефон", null=True, blank=True, unique=True)

    def __str__(self) -> str:
        return self.user.username


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username

