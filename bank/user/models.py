from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms.fields import CharField
from account.models import Account
# Create your models here.
from django.forms import ModelForm
class User(models.Model):

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    user_name = models.CharField(max_length=25)
    user_password = models.CharField(max_length=255)
    account_id = models.ForeignKey(Account,on_delete=models.CASCADE)



class RegisterForm(ModelForm):

    class Meta:
        model = User
        fields= ['first_name','last_name','user_name','user_password']