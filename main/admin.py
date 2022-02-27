from django.contrib import admin
from solo.admin import SingletonModelAdmin
from main.models import EarningHeader

admin.site.register(EarningHeader, SingletonModelAdmin)
