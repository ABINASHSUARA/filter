from django.shortcuts import render
import datetime
# Create your views here.
def filters(request):
    dt = datetime.datetime.now()
    d = {'data':'achary bala pila bbb ugfhg fjhgfyug ','c':8,'dt':dt}

    return render(request,'filters.html',d)