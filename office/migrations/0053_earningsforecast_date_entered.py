# Generated by Django 3.0 on 2022-03-21 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0052_auto_20220321_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='earningsforecast',
            name='date_entered',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
