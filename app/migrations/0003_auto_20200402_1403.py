# Generated by Django 3.0.4 on 2020-04-02 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='username',
            new_name='user',
        ),
    ]