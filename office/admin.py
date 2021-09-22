from django.contrib import admin
from . import models

admin.site.register(models.Rates)
admin.site.register(models.FinicialAnalyst)
admin.site.register(models.FinicialCompany)
admin.site.register(models.CompanyCode)
admin.site.register(models.CompanyCategory)
admin.site.register(models.RateQuarter)
admin.site.register(models.EarningsForecast)
