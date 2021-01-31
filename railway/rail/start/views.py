from django.shortcuts import render
from django.http import HttpResponse
from dash.models import profile,train
# Create your views here.

def start(request):
    stat_file=open('static\\status.txt','w')
    stat_file.write('start')
    stat_file.close()
    return render(request,'start.html')
def prereq(request):
    try:
        s_file=open('static\\status.txt','r')
        if(s_file.read() in ['dash','login']):
            b=True
        else:
            b=False
        s_file.close()
        stat_file=open('static\\status.txt','w')
        stat_file.write('prereq')
        stat_file.close()
        if(request.method=="POST"):
            return render(request,'prereq.html',{'mysql':False,'back':b})
        else:
            return render(request,'prereq.html',{'mysql':False,'back':False})
    except:
        stat_file=open('static\\status.txt','r')
        sr=stat_file.read()
        stat_file.close()
        return render(request,'problem.html',{'status':sr})


def creators(request):
    stat_file=open('static\\status.txt','r')
    sr=stat_file.read()
    stat_file.close()
    return render(request,'create.html',{'status':sr})
