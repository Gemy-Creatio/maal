# Generated by Django 3.0 on 2022-02-21 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import office.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0042_auto_20220215_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companycategory',
            name='EmpEntered',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='companycode',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='office.FinicialCompany'),
        ),
        migrations.AlterField(
            model_name='earningsforecast',
            name='CompanyEntered',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expects', to='office.FinicialCompany'),
        ),
        migrations.AlterField(
            model_name='earningsforecast',
            name='EmpEntered',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='earningsforecast',
            name='ResearchCompany',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Researchexpects', to='office.ResearchCompany'),
        ),
        migrations.AlterField(
            model_name='earningsforecast',
            name='analyst',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='office.FinicialAnalyst'),
        ),
        migrations.AlterField(
            model_name='earningsforecast',
            name='report',
            field=models.FileField(blank=True, null=True, upload_to='reportspdf/'),
        ),
        migrations.AlterField(
            model_name='finicialanalyst',
            name='EmpEntered',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='finicialanalyst',
            name='currentCompany',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='currentCompany', to='office.ResearchCompany'),
        ),
        migrations.AlterField(
            model_name='finicialcompany',
            name='EmpEntered',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='finicialcompany',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='office.CompanyCategory'),
        ),
        migrations.AlterField(
            model_name='perviouscompany',
            name='analyst',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='office.FinicialAnalyst'),
        ),
        migrations.AlterField(
            model_name='ratequarter',
            name='quaratar',
            field=models.CharField(blank=True, choices=[('الربع الأول', 'الربع الأول'), ('الربع الثانى', 'الربع الثانى'), ('الربع الثالث', 'الربع الثالث'), ('الربع الرابع', 'الربع الرابع')], default='الربع الأول', max_length=255),
        ),
        migrations.AlterField(
            model_name='ratequarter',
            name='value',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ratequarter',
            name='year',
            field=models.IntegerField(blank=True, default=office.models.current_year, null=True),
        ),
        migrations.AlterField(
            model_name='rates',
            name='AnalayticName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AnalayticName', to='office.FinicialAnalyst'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='CompanyEntered',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CompanyEntered', to='office.FinicialCompany'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='EmpEntered',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rates',
            name='ResearchCompany',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ResearchCompany', to='office.ResearchCompany'),
        ),
        migrations.AlterField(
            model_name='researchcompany',
            name='EmpEntered',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
