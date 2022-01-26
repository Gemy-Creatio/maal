import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from accounts.models import User
from django.db.models.signals import post_save


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
    logo = models.ImageField(null=True, blank=True, upload_to='logos/')
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(CompanyCategory, on_delete=models.SET_NULL, null=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    link = models.URLField(null=True, blank=True)

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


class ResearchCompany(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', ])
        ]

    def __str__(self):
        return self.name


class FinicialAnalyst(models.Model):
    logo = models.ImageField(null=True, )
    name = models.CharField(max_length=255, null=True, blank=True)
    CurrentJob = models.CharField(max_length=255, null=True, blank=True)
    currentCompany = models.ForeignKey(ResearchCompany, related_name='currentCompany', null=True,
                                       on_delete=models.SET_NULL)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    tiwtterAccount = models.CharField(max_length=255, null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Analysts"
        ordering = ["id", ]
        indexes = [
            models.Index(fields=['name', 'phone', 'tiwtterAccount', 'email'])
        ]

    def __str__(self):
        return self.name


class Rates(models.Model):
    RECOMDATION_CHOICES = (
        (1, 'زيادة الوزن'),
        (2, 'تخفيض الوزن'),
        (3, 'محايد'),

    )
    CompanyEntered = models.ForeignKey(FinicialCompany, on_delete=models.SET_NULL, related_name='CompanyEntered',
                                       null=True)
    ResearchCompany = models.ForeignKey(ResearchCompany, on_delete=models.SET_NULL, related_name='ResearchCompany',
                                        null=True)
    AnalayticName = models.ForeignKey(FinicialAnalyst, on_delete=models.SET_NULL, related_name='AnalayticName',
                                      null=True)
    Recommendation = models.SmallIntegerField(max_length=255, null=True, blank=True, choices=RECOMDATION_CHOICES)
    FairValue = models.FloatField(null=True, blank=True)
    CurrenncyValue = models.FloatField(null=True, blank=True)
    MarketValue = models.FloatField(null=True, blank=True)
    EmpEntered = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    RecommendDate = models.DateField(auto_now_add=True, null=True)
    report = models.FileField(upload_to='reportspdf/', null=True)
    changeFair = models.BooleanField(null=True)
    changeMarket = models.BooleanField(null=True)

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
    EmpEntered = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    analyst = models.ForeignKey(FinicialAnalyst, on_delete=models.CASCADE)
    CompanyEntered = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE,
                                       null=True, related_name='expects')
    ResearchCompany = models.ForeignKey(ResearchCompany, on_delete=models.CASCADE,
                                        null=True, related_name='Researchexpects')
    total_earn = models.IntegerField(blank=True, null=True)
    third2020 = models.IntegerField(blank=True, null=True)

    second2020 = models.IntegerField(blank=True, null=True)
    report = models.FileField(upload_to='reportspdf/', null=True)
    realEarn = models.IntegerField(blank=True, null=True)

    @property
    def deviationsecond2020(self):
        return (self.total_earn - self.second2020) / (self.second2020 * 100)

    @property
    def deviationthird2020(self):
        return (self.total_earn - self.third2020) / (self.third2020 * 100)

    @property
    def deviationreal(self):
        return (self.total_earn - self.realEarn) / (self.realEarn * 100)

    def __str__(self):
        return str(self.CompanyEntered.name)

    class Meta:
        indexes = [
            models.Index(fields=['analyst'])
        ]
