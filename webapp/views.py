from django.shortcuts import render
import imp
from . import allpaths
foo = imp.load_source('ML',allpaths.x)
# Create your views here.
columns = foo.get_columns()
l=[]
for i in columns:
    l.append(i)
def home(request):
    return render(request,'home.html',{'columns':l})

def submit(request):
    return render(request,'result.html')