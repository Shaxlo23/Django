from django.shortcuts import render
from . import models

# Create your views here.


def users_list(request):
    users=models.User.objects.all()
    return render(request,"app1/index.html",context={"odamlar": users})

def user_view(request,slug):
    user=models.User.objects.get(slug=slug)
    return render(request,'app1/user_view.html',context={'user': user})