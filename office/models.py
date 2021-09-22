import datetime

from django.db import models
from accounts.models import User


class CompanyCategory(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', ])
        ]

    def __str__(self):
        return self.name


class FinicialCompany(models.Model):
    logo = models.ImageField(null=True, )
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE, null=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'category', ])
        ]

    def __str__(self):
        return self.name


class CompanyCode(models.Model):
    code = models.CharField(null=True, max_length=255, blank=True)
    company = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='company', null=True)

    class Meta:
        indexes = [
            models.Index(fields=['code', 'company', ])
        ]

    def __str__(self):
        return self.code


class FinicialAnalyst(models.Model):
    logo = models.ImageField(null=True, )
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
        indexes = [
            models.Index(fields=['name', 'phone', 'tiwtterAccount', 'email'])
        ]

    def __str__(self):
        return self.name


class ResearchCompany(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', ])
        ]

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

    class Meta:
        indexes = [
            models.Index(fields=['FairValue', 'AnalayticName', 'CompanyEntered'])
        ]

    @property
    def fair_percentage(self):
        return (self.FairValue / self.CurrenncyValue) * 100

    @property
    def market_percentage(self):
        return (self.MarketValue / self.CurrenncyValue) * 100

    def __str__(self):
        return str(self.CompanyEntered)


class PerviousCompany(models.Model):
    job = models.CharField(max_length=255, null=True, blank=True, )
    analyst = models.ForeignKey(FinicialAnalyst, on_delete=models.CASCADE)
    company = models.CharField(max_length=255, null=True, blank=True, )

    class Meta:
        indexes = [
            models.Index(fields=['job', 'analyst', 'company'])
        ]

    def __str__(self):
        return self.analyst.name


def current_year():
    return datetime.date.today().year


class RateQuarter(models.Model):
    QURATARYEARS = [
        ('الربع الأول', 'الربع الأول'),
        ('الربع الثانى', 'الربع الثانى'),
        ('الربع الثالث', 'الربع الثالث'),
        ('الربع الرابع', 'الربع الرابع'),
    ]
    year = models.IntegerField(null=True, default=current_year)
    quaratar = models.CharField(max_length=255, choices=QURATARYEARS, default='الربع الأول')
    value = models.PositiveIntegerField(null=True, default=0)
    deviation_range = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.quaratar


class EarningsForecast(models.Model):
    EmpEntered = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    analyst = models.ForeignKey(FinicialAnalyst, on_delete=models.CASCADE)
    CompanyEntered = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE,
                                       null=True)
    ResearchCompany = models.ForeignKey(ResearchCompany, on_delete=models.CASCADE,
                                        null=True)
    expectYear = models.ManyToManyField(RateQuarter, null=True)
    expectvalue = models.IntegerField(blank=True, null=True)
    report = models.FileField(upload_to='reportspdf/', null=True)

    def __str__(self):
        return str(self.CompanyEntered.name)

    class Meta:
        indexes = [
            models.Index(fields=['analyst'])
        ]
