from django.shortcuts import render,redirect
from .models import CounterModel

def helloworld(request):
    return render(request,"helloworld/helloworld.html")

# Function below is passed also a variable, like it would be data context
def hellocareeria(request):
    name = "Simo"
    context = {'name': name }
    return render(request,"helloworld/hellocareeria.html",context)

def counter(request):
    obj = CounterModel.objects.filter(id = 1)[0]
    mynumber = obj.number
    context = {'number': mynumber}
    return render(request,"helloworld/counter.html",context)

def increment(request):
    obj = CounterModel.objects.filter(id = 1)[0]
    obj.number = int(obj.number) + 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def reset(request):
    obj = CounterModel.objects.filter(id = 1)[0]
    obj.number = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def decrement(request):
    obj = CounterModel.objects.filter(id = 1)[0]
    obj.number = int(obj.number) - 1 
    obj.save()
    return redirect(request.META['HTTP_REFERER'])
