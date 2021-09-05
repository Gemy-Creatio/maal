from django.db import models
from accounts.models import User


class CompanyCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class FinicialCompany(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE, null=True)
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
    currentCompany = models.ForeignKey(FinicialCompany, related_name='currentCompany', null=True,
                                       on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    tiwtterAccount = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Analysts"
        ordering = ["id", ]

    def __str__(self):
        return self.name


class ResearchCompany(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Rates(models.Model):
    CompanyEntered = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='CompanyEntered',
                                       null=True)
    ResearchCompany = models.ForeignKey(ResearchCompany, on_delete=models.CASCADE, related_name='ResearchCompany',
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
        return self.CompanyEntered.name


class PerviousCompany(models.Model):
    job = models.CharField(max_length=255, null=True, blank=True, )
    analyst = models.ForeignKey(FinicialAnalyst ,on_delete=models.CASCADE)
    company = models.CharField(max_length=255, null=True, blank=True, )

    def __str__(self):
        return self.analyst.name
