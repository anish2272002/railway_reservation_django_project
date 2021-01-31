from django.shortcuts import render
from django.http import HttpResponse
from dash.models import profile
from dash.models import train
from dash.models import ticket

# Create your views here.

def dash(request):
    stat_file=open('static\\status.txt','r')
    stat_file_read=stat_file.read()
    stat_file.close()
    if(request.method=="POST"):
        p=profile()
        p.user=request.POST['user']
        p.passwd=request.POST['passwd']
        p.fname=request.POST['fname'].upper()
        p.lname=request.POST['lname'].upper()
        p.dob=request.POST['dob']
        p.gender=request.POST['gender']
        p.phn=request.POST['phn']
        try:
            p.save()
            fil=open('static\\user.txt','w')
            ad=str(p.user+' '+p.passwd+' '+p.fname+' '+p.lname)
            fil.write(ad)
            fil.close()
            stat_file=open('static\\status.txt','w')
            stat_file.write('dash')
            stat_file.close()
            return render(request,'dash.html',{'fname':p.fname,'lname':p.lname,'train':train.objects.all()})
        except:
            if(stat_file_read=='start'):
                return render(request,'problem.html',{'status':'start'})
            elif(stat_file_read=='prereq'):
                return render(request,'problem.html',{'status':'prereq'})
            elif(stat_file_read=='dash'):
                return render(request,'problem.html',{'status':'dash'})
            else:
                return render(request,'problem.html',{'status':'start'})
    elif(request.method!="POST"):
        fil=open('static\\user.txt','r')
        filr=fil.read().split()
        fname=str(filr[2]).upper()
        lname=str(filr[3]).upper()
        fil.close()
        return render(request,'dash.html',{'fname':fname,'lname':lname,'train':train.objects.values()})
    else:
        stat_file=open('static\\status.txt','r')
        sr=stat_file.read()
        stat_file.close()
        return render(request,'problem.html',{'status':sr})

def log(request):
    stat_file=open('static\\status.txt','w')
    stat_file.write('login')
    stat_file.close()
    if(request.method=="POST"):
        usr=request.POST['username']
        passwd=request.POST['password']
        for pr in profile.objects.all():
            if(usr==pr.user and passwd==pr.passwd):
                fil=open("static\\user.txt",'w')
                dc=pr.user+' '+pr.passwd+' '+pr.fname+' '+pr.lname
                fil.write(dc)
                fil.close()
                return render(request,"login.html",{'status':True})
        else:
            return render(request,"login.html",{'status':False})
    else:
        return render(request,"login.html",{'status':0})

def trainsearch(request):
    fil=open('static\\user.txt','r')
    filr=fil.read().split()
    fname=str(filr[2]).upper()
    lname=str(filr[3]).upper()
    fil.close()
    if(request.method=='POST'):
        fro=request.POST['dash_search_from']
        to=request.POST['dash_search_to']
        date=request.POST['dash_search_date']
        data=train.objects.all().filter(tstart=fro,tend=to)
        return render(request,'trainsearch.html',{'fname':fname,'lname':lname,'train':data,'date':date})
    else:
        stat_file=open('static\\status.txt','r')
        stat_file_read=stat_file.read()
        stat_file.close()
        return render(request,'problem.html',{'status':stat_file_read})

def book(request):
    fil=open('static\\user.txt','r')
    filr=fil.read().split()
    fname=str(filr[2]).upper()
    lname=str(filr[3]).upper()
    fil.close()
    tno=request.POST['stno']
    date=request.POST['sdate']
    for tr in train.objects.all():
        if(int(tno)==tr.tno):
            return render(request,'book.html',{'fname':fname,'lname':lname,'train':tr,'date':date})

def tconfirm(request):
    tno=request.POST['stno']
    d=request.POST['date']
    if(request.POST['user']=='user'):
        fil=open('static\\user.txt','r')
        filr=fil.read().split()
        pro=profile.objects.get(user=filr[0])
        fil.close()
        u=True
    else:
        pro=None
        u=False 
    for tr in train.objects.all():
        if(int(tno)==tr.tno):
                return render(request,'confirm.html',{'user':u,'train':tr,'date':d,'userinfo':pro})
    else:
        return HttpResponse("<h1>Kill ?_? <h1>")

def ticket_status(request):
    fil=open('static\\user.txt','r')
    filr=fil.read().split()
    usr=str(filr[0])
    fname=str(filr[2]).upper()
    lname=str(filr[3]).upper()
    fil.close()
    if(request.method=="POST"):
        import random
        t=ticket()
        t.tid=random.randint(100000000000000,999999999999999)
        t.classtype=request.POST['classtype']
        if(t.classtype=='1AC'):
            t.price=random.choice([4765,5500,6068])
        elif(t.classtype=='2AC'):
            t.price=random.choice([2145,1789,3056])
        elif(t.classtype=='3AC'):
            t.price=random.choice([987,1012,1123])
        else:
            t.price=random.choice([347,456,515])
        t.start=request.POST['from']
        t.end=request.POST['to']
        t.departure=request.POST['departure']
        t.tname=request.POST['tname']
        t.pnr=random.randint(1000000000,9999999999)
        t.fname=request.POST['fname']
        t.lname=request.POST['lname']
        t.dob=str(request.POST['dob'])
        t.gender=request.POST['gender']
        t.phn=request.POST['mobile']
        t.status=True
        t.creatorid=filr[0]
        t.save()
        tk=ticket.objects.all().filter(creatorid=usr)
        return render(request,'tkstatus.html',{'fname':fname,'lname':lname,'ticket':tk})
    else:
        tk=ticket.objects.all().filter(creatorid=usr)
        return render(request,'tkstatus.html',{'fname':fname,'lname':lname,'ticket':tk})

def cancel_ticket(request):
    fil=open('static\\user.txt','r')
    filr=fil.read().split()
    usr=filr[0]
    fname=str(filr[2]).upper()
    lname=str(filr[3]).upper()
    fil.close()
    if(request.method=="POST"):
        if(request.POST['usr']==filr[0]):
            if(request.POST['passwd']==filr[1]):
                for tk in ticket.objects.all():
                    if(tk.pnr==int(request.POST['pnr'])):
                        tk.status=False
                        tk.save()
                        return render(request,'canceltk.html',{'fname':fname,'lname':lname,'ticket':ticket.objects.all().filter(creatorid=usr,status=False),'cancel':True,'cancel_tk':tk})
                else:
                    return render(request,'canceltk.html',{'fname':fname,'lname':lname,'ticket':ticket.objects.all().filter(creatorid=usr,status=False),'cancel':False})
            else:
                return render(request,'canceltk.html',{'fname':fname,'lname':lname,'ticket':ticket.objects.all().filter(creatorid=usr,status=False),'cancel':False})
        else:
            return render(request,'canceltk.html',{'fname':fname,'lname':lname,'ticket':ticket.objects.all().filter(creatorid=usr,status=False),'cancel':False})
    else:
        return render(request,'canceltk.html',{'fname':fname,'lname':lname,'ticket':ticket.objects.all().filter(creatorid=usr,status=False),'cancel':0})

def reset(request):
    fil=open('static\\user.txt','r')
    filr=fil.read().split()
    fname=str(filr[2]).upper()
    lname=str(filr[3]).upper()
    fil.close()
    if(request.method=="POST"):
        for pr in profile.objects.all():
            pr.delete()
        for tk in ticket.objects.all():
            tk.delete()
        fi=open("static\\status.txt","w")
        fi.write("start")
        fi.close()
        f=open("static\\user.txt","w")
        f.write("_ _ login _")
        f.close()
        return HttpResponse("<h1>THANK YOU <br>CLOSE THE COMMAND PROMPT WINDOW</h1>")
    else:
        return render(request,'reset.html',{'fname':fname,'lname':lname})