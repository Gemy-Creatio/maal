from django.db import models
from accounts.models import User


class FinicialCompany(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class CompanyCode(models.Model):
    code = models.CharField(null=True, max_length=255, blank=True)
    company = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='company', null=True)

    def __str__(self):
        return self.code


class FinicialAnalyst(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    CurrentJob = models.CharField(max_length=255, null=True, blank=True)
    pervCompany = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='pervCompany', null=True)
    currentCompany = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='currentCompany',
                                       null=True)
    pervJob = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    tiwtterAccount = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Rates(models.Model):
    CompanyEntered = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='CompanyEntered',
                                       null=True)
    ResearchCompany = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='ResearchCompany',
                                        null=True)
    AnalayticName = models.ForeignKey(FinicialAnalyst, on_delete=models.CASCADE, related_name='AnalayticName',
                                      null=True)
    Recommendation = models.CharField(max_length=255, null=True, blank=True, )
    FairValue = models.FloatField(null=True, blank=True)
    CurrenncyValue = models.FloatField(null=True, blank=True)
    MarketValue = models.FloatField(null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    RecommendDate = models.DateField(auto_now_add=True, null=True)
    report = models.FileField(upload_to='reportspdf/', null=True)

    @property
    def fair_percentage(self):
        return (self.FairValue / self.CurrenncyValue) * 100

    @property
    def market_percentage(self):
        return (self.MarketValue / self.CurrenncyValue) * 100

    def __str__(self):
        return self.CompanyEntered
