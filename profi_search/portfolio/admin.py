from django.contrib import admin

from profi_search.portfolio.models import Education, WorkExperience, Service, Speciality, Portfolio 

admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Service)
admin.site.register(Speciality)
admin.site.register(Portfolio)
