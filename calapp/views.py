from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'input.html')
def calculate(request):
    x=int(request.POST["t1"])
    y=int(request.POST["t2"])
    op=(request.POST["opt"])
    con_dict={}
    if op=="add":
        con_dict["res"]=x+y
    elif op=="sub":
        con_dict["res"]=x-y
    elif op=="mul":
        con_dict["res"]=x*y
    else:
        con_dict["res"]=x/y
        return render(request,'result.html',context=con_dict)
    return HttpResponse(con_dict["res"])