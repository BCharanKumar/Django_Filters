from django.shortcuts import render

# Create your views here.



def filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'i am Fan of PoWeR StaR','dt':dt,'c':5}
    return render(request,'filters.html',d)