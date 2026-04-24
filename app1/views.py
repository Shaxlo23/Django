from django.shortcuts import render
from . import models

# Create your views here.


def users_list(request):
    users=models.User.objects.all()
    return render(request,"app1/index.html",context={"odamlar": users})

def user_view(request,user_id):
    user=models.User.objects.get(pk=user_id)
    return render(request,'app1/user_view.html',context={'user': user})