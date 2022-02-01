from django.db import models
from office.models import FinicialCompany


# Create your models here.
class SeniorOwner(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    @property
    def NumberOfCompanies(self):
        return self.companies_related.all().count()

    @property
    def numberOfArrows(self):
        return self.companies_related.all().count()

    @property
    def TotalPriceArrows(self):
        price = 0
        for num in self.companies_related.all():
            price = price + num.TotalArrowPrice
        return price

    def __str__(self) -> str:
        return self.name


class CompaniesArrow(models.Model):
    company = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name="owners_arrow")
    owner = models.ForeignKey(SeniorOwner, on_delete=models.CASCADE, related_name="companies_related")
    ownRatio = models.FloatField(null=True, blank=True)
    totalOwnRatioToday = models.FloatField(null=True, blank=True)
    totalOwnRatioYesterday = models.FloatField(null=True, blank=True)
    total_arrows_owned = models.IntegerField(null=True, blank=True, default=0)

    @property
    def ChangeOwn(self):
        if self.totalOwnRatioToday is not None:
            return (self.totalOwnRatioYesterday - self.totalOwnRatioToday) / 100

    @property
    def TotalArrowPrice(self):
        if self.total_arrows_owned is None:
            return 0
        else:
            result = self.total_arrows_owned * self.company.arrow_value
            return result

    def __str__(self) -> str:
        return self.owner.name


class FinicalCompaniesArrow(models.Model):
    company = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='company_owned')
    owner = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='company_that_owned')
    numberOFArrows = models.IntegerField(null=True, blank=True)
    ownRatio = models.FloatField(null=True, blank=True)

    @property
    def TotalArrowPrice(self):
        if self.numberOFArrows is None or self.company.arrow_value is None:
            return 0
        else:
            result = self.numberOFArrows * self.company.arrow_value
            return result

    def __str__(self) -> str:
        return self.owner.name
