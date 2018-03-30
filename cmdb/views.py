from django.shortcuts import render
from cmdb import models
# Create your views here.


user_list = [

]

def index(request):
    # request.Post
    # request.Get
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        # temp = {"user":username,"pwd":password}
        # user_list.append(temp)
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username,pwd=password)
    # 从数据库中取出所有数据
    user_list = models.UserInfo.objects.all()
    return render(request,"index.html",{"data":user_list})