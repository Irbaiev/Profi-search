from django.db import models

from profi_search.users.models import Specialist


class Education(models.Model):
    specialist = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, related_name="educations"
    )
    name = models.CharField("Организация", max_length=150)
    faculty = models.CharField("Факультет", max_length=150)
    specialization = models.CharField("Специализация", max_length=150)
    start_at = models.DateField("Начало")
    end_at = models.DateField("Конец")

    def __str__(self) -> str:
        return f'Специалист: {self.specialist.user.username}, Огранизация: {self.name}, Факультет: {self.faculty}'


class Service(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE, related_name='services')
    title = models.CharField('Название',max_length=50)
    price = models.PositiveSmallIntegerField('Цена')

    def __str__(self) -> str:
        return f'Специалист: {self.specialist.user.username}, Название: {self.title}'


class WorkExperience(models.Model):
    specialist = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, related_name='workexperience', 
    )
    title = models.CharField('Профессия', max_length=100)
    description = models.TextField('Описание работы', null=True, blank=True)
    start_at = models.DateField("Начало работы")
    end_at = models.DateField("Окончание")
    organization = models.CharField('Организация', null=True, blank=True, max_length=100)
    city = models.CharField('Город', null=True, blank=True, max_length=100)
    position = models.CharField('Местонахождени', null=True, blank=True, max_length=100)

    def __str__(self) -> str:
        return f'Специалист: {self.specialist.user.username}, Профессия: {self.title}'



class Speciality(models.Model):
    specialist = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, related_name='speciality', 
    )
    title = models.CharField('Специальность', max_length=250)

    def __str__(self) -> str:
        return f'Специалист: {self.specialist.user.username}, Специальность: {self.title}'

class Portfolio(models.Model):
    specialist = models.ForeignKey(
        Specialist, on_delete=models.CASCADE, related_name='portfolio'
    )
    title = models.CharField('Название работы', max_length=100)
    image = models.ImageField(upload_to='articles/')
    description = models.TextField('Описание работы', null=True, blank=True)
    start_at = models.DateField("Начало работы")
    end_at = models.DateField("Завершение работы")
    organization = models.CharField("Организация", max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
