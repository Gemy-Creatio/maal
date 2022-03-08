from django.contrib import admin
from solo.admin import SingletonModelAdmin
from main.models import EarningHeader, EarningHeaderSecond

admin.site.register(EarningHeader, SingletonModelAdmin)

admin.site.register(EarningHeaderSecond, SingletonModelAdmin)
