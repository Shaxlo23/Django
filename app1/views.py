from django.shortcuts import render
from . import models

# Create your views here.


def hello(request):
    # users=[
    #     {'ism': 'Azizbek','familya': 'Abduraximov', 'yosh': 15},
    #     {'ism': 'Anvar','familya': 'Xusniddinov', 'yosh': 14},
    #     {'ism': 'Otabek','familya': 'Sobitjonov', 'yosh': 14},
    # ]

    users=models.User.objects.all()
    return render(request,"app1/index.html",context={"odamlar": users})