from django.contrib import admin

from . import models

admin.site.register(models.SeniorOwner)
admin.site.register(models.CompaniesArrow)

admin.site.register(models.CSVUpdate)
