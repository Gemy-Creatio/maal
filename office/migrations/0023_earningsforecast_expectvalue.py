# Generated by Django 3.0 on 2021-09-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0022_auto_20210922_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='earningsforecast',
            name='expectvalue',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
