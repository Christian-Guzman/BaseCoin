# Generated by Django 3.0.4 on 2020-04-08 18:54

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200408_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.PositiveIntegerField(validators=[app.models.is_positive]),
        ),
    ]