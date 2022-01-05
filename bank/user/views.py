from django.shortcuts import render
from account.models import *
from user.models import *
# Create your views here.

def login_view(request,*args,**kwargs):

    if not request.POST:
        return render(request,'index.html')
    else:
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')
        print("{} {}".format(user_name,user_password))
        users = User.objects.all()
        if len(users) == 0:
            register_form = RegisterForm(request.GET)
            return render(request,'register.html',{'form':register_form})
        else:
            user = User()
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            user_name = request.POST.get('user_name')
            user_password = request.POST.get('user_password')
            
            user.user_name = user_name
            user.first_name = first_name
            user.last_name = last_name
            user.user_password = user_password
            user.save()
            