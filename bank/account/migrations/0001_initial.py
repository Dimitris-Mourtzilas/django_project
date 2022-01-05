# Generated by Django 4.0.1 on 2022-01-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_balance', models.FloatField(default=0)),
                ('date_created', models.DateField(default='')),
            ],
        ),
    ]