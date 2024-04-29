from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
globalcnt = dict()
arr = ['python','java','php','R','rest','javascript','c','c++','haskel','nodejs','sql']
def index(requests):
    mydict ={
        'arr':arr
    }
    return render(requests,'index.html',context=(mydict))

def getquery(requests):
    q = requests.GET['languages']   
    if q not in globalcnt:
        globalcnt[q]=1
    else:
        globalcnt[q]+=1 
    mydict = {
        'arr':arr,
        'globalgnt':globalcnt
    }        
    
    return render(requests,'index.html',context=(mydict))


def sortdata(requests):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True))
    mydict = {
        'arr':arr,
        'globalgnt':globalcnt
    }        
    
    return render(requests,'index.html',context=(mydict))

    