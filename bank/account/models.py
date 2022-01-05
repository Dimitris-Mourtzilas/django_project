from django.db import models
from django.db.models import fields
from django.forms import ModelForm
# Create your models here.
class Account(models.Model):

    account_id = models.AutoField(primary_key=True)
    account_balance = models.FloatField(default=0)
    date_created = models.DateField(default='')
    


class AccountForm(ModelForm):

    class Meta:
        model = Account
        fields= '__all__'
