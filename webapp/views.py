from django.shortcuts import render
import imp
from . import allpaths
foo = imp.load_source('ML',allpaths.x)
# Create your views here.
columns = foo.get_columns()
l=[]
for i in columns:
    l.append(i)
l.pop(-1)
def home(request):
    return render(request,'home.html',{'columns':l})

def submit(request):
    ans=[]
    for i in l:
        x=request.POST.get(i,'off')
        if x=='on':
            x=1
        else:
            x=0
        ans.append(x)
    # print(len(ans))
    pred=foo.get_prediction(ans)
    return render(request,'result.html',{'ans':ans,'pred':pred})