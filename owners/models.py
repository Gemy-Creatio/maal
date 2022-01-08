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
        count = 0
        for num in self.companies_related.all():
            count = count + num.numberOFArrows
        return count

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
    numberOFArrows = models.IntegerField(null=True, blank=True)
    ownRatio = models.FloatField(null=True, blank=True)
    arrowPrice = models.FloatField(null=True, blank=True)
    totalOwnRatioToday = models.FloatField(null=True, blank=True)
    totalOwnRatioYesterday = models.FloatField(null=True, blank=True)

    @property
    def ChangeOwn(self):
        return (self.totalOwnRatioYesterday - self.totalOwnRatioToday) / 100

    @property
    def TotalArrowPrice(self):
        return self.numberOFArrows * self.arrowPrice

    def __str__(self) -> str:
        return self.owner.name


class FinicalCompaniesArrow(models.Model):
    company = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='company_owned')
    owner = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='company_that_owned')
    numberOFArrows = models.IntegerField(null=True, blank=True)
    ownRatio = models.FloatField(null=True, blank=True)
    arrowPrice = models.FloatField(null=True, blank=True)

    @property
    def TotalArrowPrice(self):
        return self.numberOFArrows * self.arrowPrice

    def __str__(self) -> str:
        return self.owner.name
