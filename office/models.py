from django.db import models
from accounts.models import User


class Rates(models.Model):
    CompanyEntered = models.CharField(max_length=255, null=True, blank=True, )
    ResearchCompany = models.CharField(max_length=255, null=True, blank=True, )
    AnalayticName = models.CharField(max_length=255, null=True, blank=True, )
    Recommendation = models.CharField(max_length=255, null=True, blank=True, )
    FairValue = models.FloatField(null=True, blank=True)
    CurrenncyValue = models.FloatField(null=True, blank=True)
    MarketValue = models.FloatField(null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    RecommendDate = models.DateField(auto_now_add=True)
    report = models.FileField(upload_to='reportspdf/')

    @property
    def fair_percentage(self):
        return (self.FairValue/self.CurrenncyValue) * 100

    @property
    def market_percentage(self):
        return (self.MarketValue / self.CurrenncyValue) * 100

    def __str__(self):
        return self.CompanyEntered

