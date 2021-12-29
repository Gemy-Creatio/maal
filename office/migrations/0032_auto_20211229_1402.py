# Generated by Django 3.0 on 2021-12-29 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0031_auto_20211229_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earningsforecast',
            name='EmpEntered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='finicialanalyst',
            name='EmpEntered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='finicialanalyst',
            name='currentCompany',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='currentCompany', to='office.FinicialCompany'),
        ),
        migrations.AlterField(
            model_name='finicialcompany',
            name='EmpEntered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='finicialcompany',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='office.CompanyCategory'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='AnalayticName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AnalayticName', to='office.FinicialAnalyst'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='CompanyEntered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CompanyEntered', to='office.FinicialCompany'),
        ),
        migrations.AlterField(
            model_name='rates',
            name='EmpEntered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rates',
            name='ResearchCompany',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ResearchCompany', to='office.ResearchCompany'),
        ),
        migrations.AlterField(
            model_name='researchcompany',
            name='EmpEntered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
