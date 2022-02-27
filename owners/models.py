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
    company = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name="owners_arrow", blank=True)
    owner = models.ForeignKey(SeniorOwner, on_delete=models.CASCADE, related_name="companies_related", blank=True)
    ownRatio = models.FloatField(default=1)
    totalOwnRatioToday = models.FloatField(default=1)
    totalOwnRatioYesterday = models.FloatField(default=1)
    total_arrows_owned = models.BigIntegerField(default=0)
    date = models.DateField(null=True, blank=True)
    OWNER_TYPES = (
        (1, 'فرد'),
        (2, 'شركة'),
        (3, 'مؤسسة حكومية'),
    )
    owner_type = models.SmallIntegerField(null=True, blank=True)

    @property
    def ChangeOwn(self):
        if self.totalOwnRatioToday is not None:
            return (self.totalOwnRatioYesterday - self.totalOwnRatioToday) / 100

    @property
    def TotalArrowPrice(self):
        if self.total_arrows_owned is not None:
            result = self.total_arrows_owned * self.company.arrow_value
            return result
        else:
            return 0

    def __str__(self) -> str:
        return self.owner.name


class FinicalCompaniesArrow(models.Model):
    company = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='company_owned', blank=True)
    owner = models.ForeignKey(FinicialCompany, on_delete=models.CASCADE, related_name='company_that_owned', blank=True)
    numberOFArrows = models.FloatField(default=1)
    ownRatio = models.FloatField(default=1)

    @property
    def TotalArrowPrice(self):
        if self.numberOFArrows is None or self.company.arrow_value is None:
            return 0
        else:
            result = self.numberOFArrows * self.company.arrow_value
            return result

    def __str__(self) -> str:
        return self.owner.name
