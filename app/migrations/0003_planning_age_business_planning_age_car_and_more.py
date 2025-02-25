# Generated by Django 5.0.6 on 2024-06-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_planning_alary_remove_planning_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='age_business',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_car',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_charity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_education',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_emergency_fund',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_home_renovation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_investment',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_kids',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_luxury_car',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_luxury_house',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_marriage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_medical',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_retirement',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_vacation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='age_villa',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_business',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_car',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_charity',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_education',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_emergency_fund',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_home_renovation',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_investment',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_kids',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_luxury_car',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_luxury_house',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_marriage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_medical',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_retirement',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_vacation',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='amount_villa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='planning',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
