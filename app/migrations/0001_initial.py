# Generated by Django 3.0.4 on 2020-03-19 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incoming_transactions', related_query_name='incoming_transaction', to=settings.AUTH_USER_MODEL)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outgoing_transactions', related_query_name='outgoing_transaction', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
