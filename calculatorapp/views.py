from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def submitquery(requests):
    q = requests.GET['query']
    try:
        ans = eval(q)
        mydict ={
            "q":q,
            "ans":ans,
            "error":False,
            "result":True
        }
        return render(requests,'index.html',context=(mydict))
    except:
        mydict ={
            "error":True,
            "result":False
        }
        return render(requests,'index.html',context=(mydict))
    
