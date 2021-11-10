from django.db import models
from office.models import FinicialCompany
# Create your models here.
class SeniorOwner(models.Model):
    name = models.CharField(max_length=255 , null=True , blank=True)
    description  = models.TextField(null=True , blank=True)
    def __str__(self) -> str:
        return self.name

class CompaniesArrow(models.Model):
    company = models.ForeignKey(FinicialCompany , on_delete=models.CASCADE)
    owner = models.ForeignKey(SeniorOwner , on_delete=models.CASCADE) 
    numberOFArrows = models.IntegerField(null=True , blank=True)
    def __str__(self) -> str:
        return self.owner.name