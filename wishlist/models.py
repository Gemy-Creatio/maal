from django.db import models
from accounts.models import User
from office.models import FinicialCompany
# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    wished_company = models.ForeignKey(FinicialCompany,on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.wished_company.name