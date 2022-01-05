# Generated by Django 4.0.1 on 2022-01-05 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_id',
            field=models.ForeignKey(default=-2001, on_delete=django.db.models.deletion.CASCADE, to='account.account'),
            preserve_default=False,
        ),
    ]